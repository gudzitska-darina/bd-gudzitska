--
-- PostgreSQL database dump
--

-- Dumped from database version 11.13
-- Dumped by pg_dump version 11.13

-- Started on 2021-09-25 20:32:27

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

SET default_with_oids = false;

--
-- TOC entry 205 (class 1259 OID 16517)
-- Name: bills; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.bills (
    id integer NOT NULL,
    order_id integer NOT NULL,
    product_id integer NOT NULL
);


ALTER TABLE public.bills OWNER TO postgres;

--
-- TOC entry 204 (class 1259 OID 16515)
-- Name: bills_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.bills ALTER COLUMN id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.bills_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 197 (class 1259 OID 16470)
-- Name: categories; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.categories (
    categories_id integer NOT NULL,
    name character varying NOT NULL
);


ALTER TABLE public.categories OWNER TO postgres;

--
-- TOC entry 196 (class 1259 OID 16468)
-- Name: categories_categories_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.categories ALTER COLUMN categories_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.categories_categories_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 201 (class 1259 OID 16495)
-- Name: clients; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.clients (
    client_id integer NOT NULL,
    login character varying NOT NULL,
    password character varying NOT NULL
);


ALTER TABLE public.clients OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 16493)
-- Name: clients_client_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.clients ALTER COLUMN client_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.clients_client_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 203 (class 1259 OID 16505)
-- Name: orders; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.orders (
    order_id integer NOT NULL,
    is_payed boolean NOT NULL,
    client_id integer NOT NULL
);


ALTER TABLE public.orders OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 16503)
-- Name: orders_order_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.orders ALTER COLUMN order_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.orders_order_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 199 (class 1259 OID 16480)
-- Name: products; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.products (
    product_id integer NOT NULL,
    name character varying NOT NULL,
    price numeric NOT NULL,
    category_id integer NOT NULL
);


ALTER TABLE public.products OWNER TO postgres;

--
-- TOC entry 198 (class 1259 OID 16478)
-- Name: products_product_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.products ALTER COLUMN product_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.products_product_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 2856 (class 0 OID 16517)
-- Dependencies: 205
-- Data for Name: bills; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (7, 5, 1);
INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (8, 5, 2);
INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (9, 7, 5);
INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (10, 6, 5);
INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (11, 8, 3);
INSERT INTO public.bills (id, order_id, product_id) OVERRIDING SYSTEM VALUE VALUES (12, 8, 4);


--
-- TOC entry 2848 (class 0 OID 16470)
-- Dependencies: 197
-- Data for Name: categories; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.categories (categories_id, name) OVERRIDING SYSTEM VALUE VALUES (1, 'cars');
INSERT INTO public.categories (categories_id, name) OVERRIDING SYSTEM VALUE VALUES (2, 'motobikes');
INSERT INTO public.categories (categories_id, name) OVERRIDING SYSTEM VALUE VALUES (3, 'bike');


--
-- TOC entry 2852 (class 0 OID 16495)
-- Dependencies: 201
-- Data for Name: clients; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.clients (client_id, login, password) OVERRIDING SYSTEM VALUE VALUES (1, 'mare1234', '1234');
INSERT INTO public.clients (client_id, login, password) OVERRIDING SYSTEM VALUE VALUES (2, 'sasha09', 'slkej');
INSERT INTO public.clients (client_id, login, password) OVERRIDING SYSTEM VALUE VALUES (3, 'apple432', 'sncsc');


--
-- TOC entry 2854 (class 0 OID 16505)
-- Dependencies: 203
-- Data for Name: orders; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.orders (order_id, is_payed, client_id) OVERRIDING SYSTEM VALUE VALUES (5, true, 1);
INSERT INTO public.orders (order_id, is_payed, client_id) OVERRIDING SYSTEM VALUE VALUES (6, true, 3);
INSERT INTO public.orders (order_id, is_payed, client_id) OVERRIDING SYSTEM VALUE VALUES (7, false, 2);
INSERT INTO public.orders (order_id, is_payed, client_id) OVERRIDING SYSTEM VALUE VALUES (8, false, 2);


--
-- TOC entry 2850 (class 0 OID 16480)
-- Dependencies: 199
-- Data for Name: products; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.products (product_id, name, price, category_id) OVERRIDING SYSTEM VALUE VALUES (1, 'McLaren', 1500000, 1);
INSERT INTO public.products (product_id, name, price, category_id) OVERRIDING SYSTEM VALUE VALUES (2, 'Lotos', 800000, 1);
INSERT INTO public.products (product_id, name, price, category_id) OVERRIDING SYSTEM VALUE VALUES (3, 'Dodge', 70000, 1);
INSERT INTO public.products (product_id, name, price, category_id) OVERRIDING SYSTEM VALUE VALUES (4, 'Yamaha', 20000, 2);
INSERT INTO public.products (product_id, name, price, category_id) OVERRIDING SYSTEM VALUE VALUES (5, 'Krossbikes', 150, 3);


--
-- TOC entry 2862 (class 0 OID 0)
-- Dependencies: 204
-- Name: bills_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.bills_id_seq', 12, true);


--
-- TOC entry 2863 (class 0 OID 0)
-- Dependencies: 196
-- Name: categories_categories_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.categories_categories_id_seq', 3, true);


--
-- TOC entry 2864 (class 0 OID 0)
-- Dependencies: 200
-- Name: clients_client_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.clients_client_id_seq', 3, true);


--
-- TOC entry 2865 (class 0 OID 0)
-- Dependencies: 202
-- Name: orders_order_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.orders_order_id_seq', 8, true);


--
-- TOC entry 2866 (class 0 OID 0)
-- Dependencies: 198
-- Name: products_product_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.products_product_id_seq', 5, true);


--
-- TOC entry 2721 (class 2606 OID 16521)
-- Name: bills bills_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT bills_pkey PRIMARY KEY (id);


--
-- TOC entry 2713 (class 2606 OID 16477)
-- Name: categories categories_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.categories
    ADD CONSTRAINT categories_pkey PRIMARY KEY (categories_id);


--
-- TOC entry 2717 (class 2606 OID 16502)
-- Name: clients clients_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.clients
    ADD CONSTRAINT clients_pkey PRIMARY KEY (client_id);


--
-- TOC entry 2719 (class 2606 OID 16509)
-- Name: orders orders_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT orders_pkey PRIMARY KEY (order_id);


--
-- TOC entry 2715 (class 2606 OID 16487)
-- Name: products products_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT products_pkey PRIMARY KEY (product_id);


--
-- TOC entry 2723 (class 2606 OID 16510)
-- Name: orders fk_client; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.orders
    ADD CONSTRAINT fk_client FOREIGN KEY (client_id) REFERENCES public.clients(client_id);


--
-- TOC entry 2724 (class 2606 OID 16522)
-- Name: bills fk_order; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT fk_order FOREIGN KEY (order_id) REFERENCES public.orders(order_id);


--
-- TOC entry 2725 (class 2606 OID 16527)
-- Name: bills fk_product; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.bills
    ADD CONSTRAINT fk_product FOREIGN KEY (product_id) REFERENCES public.products(product_id);


--
-- TOC entry 2722 (class 2606 OID 16488)
-- Name: products ft_cat; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.products
    ADD CONSTRAINT ft_cat FOREIGN KEY (category_id) REFERENCES public.categories(categories_id);


-- Completed on 2021-09-25 20:32:28

--
-- PostgreSQL database dump complete
--

