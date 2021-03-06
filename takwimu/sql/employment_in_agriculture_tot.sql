--
-- PostgreSQL database dump
--

-- Dumped from database version 10.5
-- Dumped by pg_dump version 10.5

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;

ALTER TABLE IF EXISTS ONLY public.employment_in_agriculture_tot DROP CONSTRAINT IF EXISTS pk_employment_in_agriculture_tot;
DROP TABLE IF EXISTS public.employment_in_agriculture_tot;
SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: employment_in_agriculture_tot; Type: TABLE; Schema: public; Owner: -
--

CREATE TABLE public.employment_in_agriculture_tot (
    geo_level character varying(15) NOT NULL,
    geo_code character varying(10) NOT NULL,
    geo_version character varying(100) DEFAULT ''::character varying NOT NULL,
    employment_in_agriculture_tot_year character varying(128) NOT NULL,
    total numeric
);


--
-- Data for Name: employment_in_agriculture_tot; Type: TABLE DATA; Schema: public; Owner: -
--

COPY public.employment_in_agriculture_tot (geo_level, geo_code, geo_version, employment_in_agriculture_tot_year, total) FROM stdin;
country	KE	2009	1998	45.797
country	KE	2009	1999	45.655
country	KE	2009	2000	48.954
country	KE	2009	2001	51.494
country	KE	2009	2002	54.208
country	KE	2009	2003	56.73
country	KE	2009	2004	59.016
country	KE	2009	2005	61.064
country	KE	2009	2006	60.509
country	KE	2009	2007	60.084
country	KE	2009	2008	60.176
country	KE	2009	2009	60.106
country	KE	2009	2010	59.695
country	KE	2009	2011	59.507
country	KE	2009	2012	59.138
country	KE	2009	2013	58.709
country	KE	2009	2014	58.374
country	KE	2009	2015	58.311
country	KE	2009	2016	58.17
country	KE	2009	2017	57.834
country	KE	2009	2018	57.454
country	KE	2009	2019	57.032
country	NG	2009	1999	48.151
country	NG	2009	2000	48.436
country	NG	2009	2001	47.700
country	NG	2009	2002	48.331
country	NG	2009	2003	47.726
country	NG	2009	2004	45.555
country	NG	2009	2005	44.912
country	NG	2009	2006	43.717
country	NG	2009	2007	42.860
country	NG	2009	2008	42.216
country	NG	2009	2009	41.067
country	NG	2009	2010	40.778
country	NG	2009	2011	40.185
country	NG	2009	2012	39.320
country	NG	2009	2013	38.271
country	NG	2009	2014	37.698
country	NG	2009	2015	37.080
country	NG	2009	2016	36.911
country	NG	2009	2017	36.808
country	NG	2009	2018	36.616
country	NG	2009	2019	36.384
country	ZA	2009	1999	10
country	ZA	2009	2000	9.93
country	ZA	2009	2001	9.72
country	ZA	2009	2002	10.9
country	ZA	2009	2003	9.91
country	ZA	2009	2004	9.06
country	ZA	2009	2005	7.04
country	ZA	2009	2006	6.78
country	ZA	2009	2007	6.62
country	ZA	2009	2008	5.66
country	ZA	2009	2009	5.07
country	ZA	2009	2010	4.86
country	ZA	2009	2011	4.6
country	ZA	2009	2012	4.84
country	ZA	2009	2013	4.98
country	ZA	2009	2014	4.65
country	ZA	2009	2015	5.61
country	ZA	2009	2016	5.57
country	ZA	2009	2017	5.22
country	ZA	2009	2018	5.16
country	ZA	2009	2019	5.09
country	ET	2009	1999	76.4
country	ET	2009	2000	76.4
country	ET	2009	2001	76.5
country	ET	2009	2002	76.9
country	ET	2009	2003	78.1
country	ET	2009	2004	78.2
country	ET	2009	2005	78.1
country	ET	2009	2006	77.4
country	ET	2009	2007	76.6
country	ET	2009	2008	75.9
country	ET	2009	2009	75.3
country	ET	2009	2010	73.9
country	ET	2009	2011	72.8
country	ET	2009	2012	72.3
country	ET	2009	2013	71
country	ET	2009	2014	70
country	ET	2009	2015	68.9
country	ET	2009	2016	68
country	ET	2009	2017	67.1
country	ET	2009	2018	66.2
country	ET	2009	2019	65.3
country	SN	2009	1999	48.8
country	SN	2009	2000	48.8
country	SN	2009	2001	48.5
country	SN	2009	2002	47.7
country	SN	2009	2003	46.9
country	SN	2009	2004	45.6
country	SN	2009	2005	44.7
country	SN	2009	2006	43.6
country	SN	2009	2007	42.3
country	SN	2009	2008	41.6
country	SN	2009	2009	41
country	SN	2009	2010	39.9
country	SN	2009	2011	38.6
country	SN	2009	2012	37.5
country	SN	2009	2013	36.2
country	SN	2009	2014	34.8
country	SN	2009	2015	33.3
country	SN	2009	2016	33
country	SN	2009	2017	32.5
country	SN	2009	2018	32
country	SN	2009	2019	31.5
\.


--
-- Name: employment_in_agriculture_tot pk_employment_in_agriculture_tot; Type: CONSTRAINT; Schema: public; Owner: -
--

ALTER TABLE ONLY public.employment_in_agriculture_tot
    ADD CONSTRAINT pk_employment_in_agriculture_tot PRIMARY KEY (geo_level, geo_code, geo_version, employment_in_agriculture_tot_year);


--
-- PostgreSQL database dump complete
--
