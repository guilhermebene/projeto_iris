--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.5
-- Dumped by pg_dump version 9.6.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: postgres; Type: COMMENT; Schema: -; Owner: postgres
--

COMMENT ON DATABASE postgres IS 'default administrative connection database';


--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: locais; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE locais (
    nome_local character varying(128) NOT NULL,
    complemento character varying(128)
);


ALTER TABLE locais OWNER TO postgres;

--
-- Name: objeto_esta_em_local; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE objeto_esta_em_local (
    id_objeto integer NOT NULL,
    nome_local character varying(128) NOT NULL
);


ALTER TABLE objeto_esta_em_local OWNER TO postgres;

--
-- Name: objeto_pertence_a_unidade; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE objeto_pertence_a_unidade (
    id_objeto integer NOT NULL,
    id_unidade integer NOT NULL
);


ALTER TABLE objeto_pertence_a_unidade OWNER TO postgres;

--
-- Name: objetos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE objetos (
    num_patrimonio integer NOT NULL,
    nome_objeto character varying(128) NOT NULL,
    situacao character varying(128),
    utilizacao character varying(128),
    marca character varying(128),
    modelo character varying(128),
    tipo character varying(128)
);


ALTER TABLE objetos OWNER TO postgres;

--
-- Name: responsaveis; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE responsaveis (
    num_responsavel integer NOT NULL,
    nome_responsavel character varying(128) NOT NULL,
    email_responsavel character varying(128),
    telefone_responsavel character varying(32)
);


ALTER TABLE responsaveis OWNER TO postgres;

--
-- Name: responsavel_e_responsavel_por; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE responsavel_e_responsavel_por (
    id_responsavel integer NOT NULL,
    id_objeto integer NOT NULL
);


ALTER TABLE responsavel_e_responsavel_por OWNER TO postgres;

--
-- Name: unidade_tem_local; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE unidade_tem_local (
    id_unidade integer NOT NULL,
    nome_local character varying(128) NOT NULL
);


ALTER TABLE unidade_tem_local OWNER TO postgres;

--
-- Name: unidades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE unidades (
    num_unidade integer NOT NULL,
    nome_unidade character varying(128) NOT NULL
);


ALTER TABLE unidades OWNER TO postgres;

--
-- Name: locais locais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY locais
    ADD CONSTRAINT locais_pkey PRIMARY KEY (nome_local);


--
-- Name: objeto_esta_em_local objeto_esta_em_local_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_esta_em_local
    ADD CONSTRAINT objeto_esta_em_local_pkey PRIMARY KEY (id_objeto, nome_local);


--
-- Name: objeto_pertence_a_unidade objeto_pertence_a_unidade_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_pertence_a_unidade
    ADD CONSTRAINT objeto_pertence_a_unidade_pkey PRIMARY KEY (id_objeto, id_unidade);


--
-- Name: objetos objetos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objetos
    ADD CONSTRAINT objetos_pkey PRIMARY KEY (num_patrimonio);


--
-- Name: responsaveis responsaveis_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY responsaveis
    ADD CONSTRAINT responsaveis_pkey PRIMARY KEY (num_responsavel);


--
-- Name: responsavel_e_responsavel_por responsavel_e_responsavel_por_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY responsavel_e_responsavel_por
    ADD CONSTRAINT responsavel_e_responsavel_por_pkey PRIMARY KEY (id_responsavel, id_objeto);


--
-- Name: unidade_tem_local unidade_tem_local_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unidade_tem_local
    ADD CONSTRAINT unidade_tem_local_pkey PRIMARY KEY (id_unidade, nome_local);


--
-- Name: unidades unidades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unidades
    ADD CONSTRAINT unidades_pkey PRIMARY KEY (num_unidade);


--
-- Name: objeto_esta_em_local objeto_esta_em_local_id_objeto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_esta_em_local
    ADD CONSTRAINT objeto_esta_em_local_id_objeto_fkey FOREIGN KEY (id_objeto) REFERENCES objetos(num_patrimonio);


--
-- Name: objeto_esta_em_local objeto_esta_em_local_nome_local_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_esta_em_local
    ADD CONSTRAINT objeto_esta_em_local_nome_local_fkey FOREIGN KEY (nome_local) REFERENCES locais(nome_local);


--
-- Name: objeto_pertence_a_unidade objeto_pertence_a_unidade_id_objeto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_pertence_a_unidade
    ADD CONSTRAINT objeto_pertence_a_unidade_id_objeto_fkey FOREIGN KEY (id_objeto) REFERENCES objetos(num_patrimonio);


--
-- Name: objeto_pertence_a_unidade objeto_pertence_a_unidade_id_unidade_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY objeto_pertence_a_unidade
    ADD CONSTRAINT objeto_pertence_a_unidade_id_unidade_fkey FOREIGN KEY (id_unidade) REFERENCES unidades(num_unidade);


--
-- Name: responsavel_e_responsavel_por responsavel_e_responsavel_por_id_objeto_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY responsavel_e_responsavel_por
    ADD CONSTRAINT responsavel_e_responsavel_por_id_objeto_fkey FOREIGN KEY (id_objeto) REFERENCES objetos(num_patrimonio);


--
-- Name: responsavel_e_responsavel_por responsavel_e_responsavel_por_id_responsavel_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY responsavel_e_responsavel_por
    ADD CONSTRAINT responsavel_e_responsavel_por_id_responsavel_fkey FOREIGN KEY (id_responsavel) REFERENCES responsaveis(num_responsavel);


--
-- Name: unidade_tem_local unidade_tem_local_id_unidade_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unidade_tem_local
    ADD CONSTRAINT unidade_tem_local_id_unidade_fkey FOREIGN KEY (id_unidade) REFERENCES unidades(num_unidade);


--
-- Name: unidade_tem_local unidade_tem_local_nome_local_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unidade_tem_local
    ADD CONSTRAINT unidade_tem_local_nome_local_fkey FOREIGN KEY (nome_local) REFERENCES locais(nome_local);


--
-- PostgreSQL database dump complete
--

