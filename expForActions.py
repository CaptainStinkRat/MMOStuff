import argparse



def main():
    parser = argparse.ArgumentParser(description="Checking experience rates for items")

    parser.add_argument("skill",help="Skill you are leveling")
    parser.add_argument("method",help="Item to calculate rates for")
    parser.add_argument("num",help='Number of items to be processed')
    args = parser.parse_args()
    if args.skill == "cooking":
        if args.method == "trout":
            totalExp = int(args.num) * 75
            if args.startLevel == 1:
                expStart = 0
        	if args.startlevel == 2:
                expStart = 83
            if args.startLevel == 3:
                expStart = 174
            if args.startLevel == 4:
                expStart = 276
            if args.startLevel == 5:
                expStart = 388
            if args.startLevel == 6
            43	50,339	4.8K	85	3,258,594	307.2K
	44	55,649	5.3K	86	3,597,792	339.2K
	45	61,512	5.9K	87	3,972,294	374.5K
4	276	102	46	67,983	6.5K	88	4,385,776	413.5K
5	388	112	47	75,127	7.1K	89	4,842,295	456.5K
6	512	124	48	83,014	7.9K	90	5,346,332	504K
7	650	138	49	91,721	8.7K	91	5,902,831	556.5K
8	801	151	50	101,333	9.6K	92	6,517,253	614.4K
9	969	168	51	111,945	10.6K	93	7,195,629	678.4K
10	1,154	185	52	123,660	11.7K	94	7,944,614	749K
11	1,358	204	53	136,594	12.9K	95	8,771,558	826.9K
12	1,584	226	54	150,872	14.3K	96	9,684,577	913K
13	1,833	249	55	166,636	15.8K	97	10,692,629	1M
14	2,107	274	56	184,040	17.4K	98	11,805,606	1.1M
15	2,411	304	57	203,254	19.2K	99	13,034,431	1.2M
16	2,746	335	58	224,466	21.2K	
17	3,115	369	59	247,886	23.4K	
18	3,523	408	60	273,742	25.9K	
19	3,973	450	61	302,288	28.5K	
20	4,470	497	62	333,804	31.5K	
21	5,018	548	63	368,599	34.8K	
22	5,624	606	64	407,015	38.4K	
23	6,291	667	65	449,428	42.4K	
24	7,028	737	66	496,254	46.8K	
25	7,842	814	67	547,953	51.7K	
26	8,740	898	68	605,032	57.1K	
27	9,730	990	69	668,051	63K	
28	10,824	1.1K	70	737,627	69.6K	
29	12,031	1.2K	71	814,445	76.8K	
30	13,363	1.3K	72	899,257	84.8K	
31	14,833	1.5K	73	992,895	93.6K	
32	16,456	1.6K	74	1,096,278	103.4K	
33	18,247	1.8K	75	1,210,421	114.1K	
34	20,224	2K	76	1,336,443	126K	
35	22,406	2.2K	77	1,475,581	139.1K	
36	24,815	2.4K	78	1,629,200	153.6K	
37	27,473	2.7K	79	1,798,808	169.6K	
38	30,408	2.9K	80	1,986,068	187.3K	
39	33,648	3.2K	81	2,192,818	206.8K	
40	37,224	3.6K	82	2,421,087	228.3K	
41	41,171	3.9K	83	2,673,114	252K	
42	45,529	4.4K	84	2,951,373	278.3K	
            print(f'That comes out to {totalExp} experience.')


if __name__=="__main__":
    main()