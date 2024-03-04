from subprocess import check_output

species_array = ["homo_sapiens", "pan_troglodytes", "pongo_abelii", "gorilla_gorilla", "macaca_mulatta", "callithrix_jacchus", "bos_taurus", "canis_familiaris", "equus_caballus", "felis_catus", "ovis_aries", "sus_scrofa", "oryctolagus_cuniculus", "rattus_norvegicus", "mus_caroli", "mus_pahari", "mus_musculus"]
path = "/homes/varshith/maf_files/1/testmafs/HAL_Files/"
for ele in species_array[1:-5]:
    s = check_output(["find", path, "-name", "*{0}*".format(ele)])
    print s