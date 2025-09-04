lista_med_saker = [1, True, 5.5, "Hello world", False]

# Tar de 3 första sakerna i listan
tar_dem_tre_första = lista_med_saker[:3]
print(tar_dem_tre_första)

# tar de tre sista sakerna i listan
tar_dem_tre_sista = lista_med_saker[2:]
print(tar_dem_tre_sista)

# tar de tre sista sakerna i listan omvänt
# tar_dem_tre_sista_omvänt = lista_med_saker[2:][::-1] # <-- bästa alternativet 
tar_dem_tre_sista_omvänt = lista_med_saker[-1:1:-1] # <-- för att endast använda en slice 
print(tar_dem_tre_sista_omvänt)