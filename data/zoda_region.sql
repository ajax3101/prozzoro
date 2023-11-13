--
-- PostgreSQL database dump
--

-- Dumped from database version 12.12
-- Dumped by pg_dump version 12.12

-- Started on 2023-11-13 03:11:06

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 224 (class 1259 OID 17339)
-- Name: zoda_region; Type: TABLE; Schema: public; Owner: zoda
--

CREATE TABLE public.zoda_region (
    id bigint NOT NULL,
    name character varying(255) NOT NULL
);


ALTER TABLE public.zoda_region OWNER TO zoda;

--
-- TOC entry 223 (class 1259 OID 17337)
-- Name: zoda_region_id_seq; Type: SEQUENCE; Schema: public; Owner: zoda
--

ALTER TABLE public.zoda_region ALTER COLUMN id ADD GENERATED BY DEFAULT AS IDENTITY (
    SEQUENCE NAME public.zoda_region_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2878 (class 0 OID 17339)
-- Dependencies: 224
-- Data for Name: zoda_region; Type: TABLE DATA; Schema: public; Owner: zoda
--

INSERT INTO public.zoda_region (id, name) VALUES (0, 'Обласна ланка');
INSERT INTO public.zoda_region (id, name) VALUES (1, 'Бердянський район');
INSERT INTO public.zoda_region (id, name) VALUES (2, 'Василівський район');
INSERT INTO public.zoda_region (id, name) VALUES (3, 'Запорізький район');
INSERT INTO public.zoda_region (id, name) VALUES (4, 'Мелітопольський район');
INSERT INTO public.zoda_region (id, name) VALUES (5, 'Пологівський район');


--
-- TOC entry 2884 (class 0 OID 0)
-- Dependencies: 223
-- Name: zoda_region_id_seq; Type: SEQUENCE SET; Schema: public; Owner: zoda
--

SELECT pg_catalog.setval('public.zoda_region_id_seq', 1, false);


-- Completed on 2023-11-13 03:11:06

--
-- PostgreSQL database dump complete
--
