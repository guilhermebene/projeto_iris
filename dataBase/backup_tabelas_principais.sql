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
    nome_local integer NOT NULL,
    complemento character varying(128)
);


ALTER TABLE locais OWNER TO postgres;

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
    nome_responsavel character varying(128),
    email_responsavel character varying(128),
    telefone_responsavel character varying(32)
);


ALTER TABLE responsaveis OWNER TO postgres;

--
-- Name: unidades; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE unidades (
    num_unidade integer NOT NULL,
    nome_unidade character varying(128) NOT NULL
);


ALTER TABLE unidades OWNER TO postgres;

--
-- Data for Name: locais; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY locais (nome_local, complemento) FROM stdin;
\.


--
-- Data for Name: objetos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY objetos (num_patrimonio, nome_objeto, situacao, utilizacao, marca, modelo, tipo) FROM stdin;
\.


--
-- Data for Name: responsaveis; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY responsaveis (num_responsavel, nome_responsavel, email_responsavel, telefone_responsavel) FROM stdin;
\.


--
-- Data for Name: unidades; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY unidades (num_unidade, nome_unidade) FROM stdin;
\.


--
-- Name: locais locais_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY locais
    ADD CONSTRAINT locais_pkey PRIMARY KEY (nome_local);


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
-- Name: unidades unidades_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY unidades
    ADD CONSTRAINT unidades_pkey PRIMARY KEY (num_unidade);


--
-- PostgreSQL database dump complete
--

