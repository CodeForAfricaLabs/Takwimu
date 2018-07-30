--
-- PostgreSQL database dump
--

-- Dumped from database version 10.0
-- Dumped by pg_dump version 10.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

ALTER TABLE IF EXISTS ONLY public.population_year DROP CONSTRAINT IF EXISTS pk_population_year;
DROP TABLE IF EXISTS public.population_year;
SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: population_year; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.population_year (
    geo_level character varying(15) NOT NULL,
    geo_code character varying(10) NOT NULL,
    geo_version character varying(100) DEFAULT ''::character varying NOT NULL,
    "Population_Year" character varying(128) NOT NULL,
    total integer
);


--
-- Data for Name: population_year; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.population_year (geo_level, geo_code, geo_version, "Population_Year", total) FROM stdin;
country	NG	2009	2000	122352009
country	SN	2009	2000	9884052
country	TZ	2009	2000	34178042
country	NG	2009	2001	125463434
country	SN	2009	2001	10134497
country	TZ	2009	2001	35117019
country	NG	2009	2002	128666710
country	SN	2009	2002	10396861
country	TZ	2009	2002	36105808
country	NG	2009	2003	131972533
country	SN	2009	2003	10670990
country	TZ	2009	2003	37149072
country	NG	2009	2004	135393616
country	SN	2009	2004	10955944
country	TZ	2009	2004	38249984
country	NG	2009	2005	138939478
country	SN	2009	2005	11251266
country	TZ	2009	2005	39410545
country	NG	2009	2006	142614094
country	SN	2009	2006	11556763
country	TZ	2009	2006	40634948
country	NG	2009	2007	146417024
country	SN	2009	2007	11873557
country	TZ	2009	2007	41923715
country	NG	2009	2008	150347390
country	SN	2009	2008	12203957
country	TZ	2009	2008	43270144
country	NG	2009	2009	154402181
country	SN	2009	2009	12550917
country	TZ	2009	2009	44664231
country	NG	2009	2010	158578261
country	SN	2009	2010	12916229
country	TZ	2009	2010	46098591
country	NG	2009	2011	162877076
country	SN	2009	2011	13300910
country	TZ	2009	2011	47570902
country	NG	2009	2012	167297284
country	SN	2009	2012	13703513
country	TZ	2009	2012	49082997
country	NG	2009	2013	171829303
country	SN	2009	2013	14120320
country	TZ	2009	2013	50636595
country	NG	2009	2014	176460502
country	SN	2009	2014	14546111
country	TZ	2009	2014	52234869
country	NG	2009	2015	181181744
country	SN	2009	2015	14976994
country	TZ	2009	2015	53879957
country	NG	2009	2016	185989640
country	SN	2009	2016	15411614
country	TZ	2009	2016	55572201
\.


--
-- Name: population_year pk_population_year; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.population_year
    ADD CONSTRAINT pk_population_year PRIMARY KEY (geo_level, geo_code, geo_version, "Population_Year");


--
-- PostgreSQL database dump complete
--
