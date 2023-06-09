from .models import UrlJuegos,Telefonos,Favoritos,Favoritos_UrlJuegos,Historiales,RamsVelocidades,Rams,Procesadores,SistemasOperativos,GraficasGb,GraficasVelocidades,Graficas,Dispositivos

def obtenerCara(ar:list):
  g=0
  r=0
  c=0
  so=0
  st=0
  # ---------
  graficas=[]
  canGraficas=-1
  rams=[]
  canRams=-1
  cpu=[]
  canCpu=-1
  sisOp=[]
  canSis=-1
  storage=[]
  canSto=-1
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
      if 'type' in linea and 'unknown' in linea:
        del rams[canRams]
        canRams-=1
        r=0
        continue
      if 'format' in linea and 'unknown' in linea:
        del rams[canRams]
        canRams-=1
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
        storage[canSto]['capacidad']=linea.strip()[8:].strip()
      # para que no lea el tipo de bus
      if 'Type' in linea and not 'Bus' in linea:
        storage[canSto]['tipo']=linea.strip()[4:].strip()
      if 'Volume' in linea and not storage[canSto].get('disponible'):
        gbDiscoPosiciones=[linea.index(',')+1,linea.index('GBytes')]
        gbDisco=float(linea[gbDiscoPosiciones[0]:gbDiscoPosiciones[1]].strip())
        pare=[linea.index('(')+1,linea.index('percent')-1]
        porcentaje=float(linea[pare[0]:pare[1]])
        disponible=str(round((gbDisco*(porcentaje/100)),2))+' GB'
        storage[canSto]['disponible']=disponible
        continue
      
      if 'Volume' in linea:
        if storage[canSto].get('disponible'):
          disponible=storage[canSto].get('disponible')

          gbDiscoPosiciones=[linea.index(',')+1,linea.index('GBytes')]
          gbDisco=float(linea[gbDiscoPosiciones[0]:gbDiscoPosiciones[1]].strip())
          pare=[linea.index('(')+1,linea.index('percent')-1]
          porcentaje=float(linea[pare[0]:pare[1]])
          disponible2=str(round((gbDisco*(porcentaje/100)),2))+' GB'

          if not disponible2==disponible:
            storage[canSto]['disponible2']=disponible2
            st=0

  return {'graficas':graficas,'rams':rams,'procesador':cpu,'sisOpe':sisOp,'discos':storage}

def guardarCara(carate:dict):
  #guardar grafica(s)
  graficas=carate['graficas']

  #recorro las graficas y empiezo a guardar los valores
  for grafica in graficas:
    #creo el objeto de la grafica a guardar
    g=Graficas()
    if grafica.get('tamano'):
      #extraigo el tamaño si existe, le quito el gb y lo convierto en numero float
      if 'MB' in grafica.get('tamano'):
        tamano=float((float(grafica.get('tamano').replace('MB','').strip()))//1000)
      else:
        tamano=float(grafica.get('tamano').replace('GB','').strip())
      # lo creo sino existe, de lo contrario solo lo obtengo
      objTama,creado = GraficasGb.objects.get_or_create(gb=tamano)
      # lo relaciono con objeto creado
      g.gb=objTama
      if creado:
        print('tamaño de grafica agregado\n')
    
    if grafica.get('velocidadNucleo'):
      #extraigo la velocidad si existe, le quito el mhz y lo convierto en numero int
      vel=int(float(grafica.get('velocidadNucleo').replace('MHz','').strip()))
      
      # lo creo sino existe, de lo contrario solo lo obtengo
      objVel,creado=GraficasVelocidades.objects.get_or_create(velocidadMhz=vel)
      # lo relaciono con objeto creado
      g.velocidad=objVel
      if creado:
        print('velocidad de grafica agregada\n')
    
    if grafica.get('cantidadNucleos'):
      # obtengo la cantidad de nucleos y lo agrego al objeto creado
      nucleos=int(grafica.get('cantidadNucleos'))
      if nucleos != 0:
        g.nucleos=nucleos

    
    if grafica.get('nombre'):
      # obtengo la grafica por su nombre, si no existe, la creo con sus valores, de lo contrario no hago nada
      creado=Graficas.objects.filter(nombre__exact=grafica.get('nombre')).exists()
      if not creado:
        g.nombre=grafica.get('nombre')
        g.save()
        print('Nombre de grafica guardado\n')
    
  rams=carate['rams']
  procesador=carate['procesador']
  sistema=carate['sisOpe']
  discos=carate['discos']
