def obtenerCara(ar:list):
  g=0
  r=0
  c=0
  so=0
  st=0
  # ---------
  graficas=['graficas']
  canGraficas=0
  rams=['rams']
  canRams=0
  cpu=['procesador']
  canCpu=0
  sisOp=['sistema operativo']
  canSis=0
  storage=['discos']
  canSto=0
  for linea in ar:
    # informacion de las graficas
    if 'Display adapter' in linea:
        # creo cada dict dentro de cada arreglo y agrego los datos, porque hay unos que no tiene todos, entonces no podria utilizar el append(dict) porque no podria saber donde hacerlo precisamente
        graficas.append({})
        canGraficas+=1
        if g==0:
          g=1
    if g!=0:
      if 'Name' in linea:
         graficas[canGraficas]['nombre']=linea.strip()[4:].strip()
      if 'Memory size' in linea:
        graficas[canGraficas]['tamano']=linea.strip()[11:].strip()
      if 'Cores' in linea:
        graficas[canGraficas]['cantidadNucleos']=linea.strip()[5:].strip()
      if 'Core clock' in linea:
        graficas[canGraficas]['velocidadNucleo']=linea.strip()[10:].strip()
      if 'Memory clock' in linea:
        graficas[canGraficas]['velocidadMemoria']=linea.strip()[12:].strip()
        g=0
    
    #informacion de las rams
    if 'DMI Memory Device' in linea:
      rams.append({})
      canRams+=1
      if r==0:
        r=1
    if r!=0:
      if 'format' in linea and 'unknown' in linea:
        del rams[canRams]
        r=0
        continue
      if 'type' in linea:
        rams[canRams]['tipo']=linea.strip()[4:].strip()
      if 'size' in linea:
        rams[canRams]['tamano']=linea.strip()[4:].strip()
      if 'speed' in linea:
        rams[canRams]['velocidad']=linea.strip()[5:].strip()
      if linea.strip()=='':
        r=0
    # informacion del procesador
    if 'DMI Processor' in linea:
      cpu.append({})
      canCpu+=1
      if c==0:
        c=1
    if c!=0:
      if 'model' in linea:
        cpu[canCpu]['modelo']=linea.strip()[5:].strip()
      if 'clock speed' in linea and 'max' not in linea:
        cpu[canCpu]['velocidad']=linea.strip()[11:].strip()
      if 'max clock speed' in linea:
        cpu[canCpu]['velocidadMaxima']=linea.strip()[15:].strip()
        c=0
    # informacion del sistema operativo
    if 'Software' in linea:
      sisOp.append({})
      canSis+=1
      if st==0:
        st=1
    if st!=0:
      if 'Windows Version' in linea:
        # el segundo windows de la linea tiene un espacio atras, el primero que es el que no quiero, no tiene ese espacio
        bit = linea.index(' Windows')+12
        sisOp[canSis]['nombre']=linea.strip()[15:bit].strip()
        st=0
    # espacio
    if 'Drive	' in linea:
      storage.append({})
      canSto+=1
      if st==0:
        st=1
    if st!=0:
      if 'Capacity' in linea:
        gb=linea.index('GB')-1
        capacity=float(linea.strip()[8:gb].strip())
        storage[canSto]['capacidad']=linea.strip()[8:].strip()
      # para que no lea el tipo de bus
      if 'Type' in linea and not 'Bus' in linea:
        storage[canSto]['tipo']=linea.strip()[4:].strip()
      if 'Volume' in linea:
        pare=[linea.index('(')+1,linea.index('percent')-1]
        porcentaje=float(linea[pare[0]:pare[1]])
        disponible=round((capacity*(porcentaje/100)),2)
        storage[canSto]['disponible']=str(disponible)+'GB'
        st=0

  return [graficas,rams,cpu,sisOp,storage]
