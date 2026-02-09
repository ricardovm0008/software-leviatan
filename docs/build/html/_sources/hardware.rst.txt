===================================
Hardware
===================================

El Laboratorio Nacional de Supercómputo del Sureste de México (LNS) cuenta con varios segmentos de cómputo científico de alto rendimiento.


----

Cluster Cuetlaxcoapan
===================================

--------------------------
:Arquitectura: Intel Xeon Haswell
:Sistema Operativo: CentOS 6.6
:Total de Núcleos: 2,952 núcleos de procesamiento
:Almacenamiento: 240 TB de espacio total
:Red: Infiniband 56 Gbps (punto a punto)

Nodos de Cálculo
-----------------

.. list-table::
   :widths: 20 15 20 20 25
   :header-rows: 1
   :align: center

   * - Tipo
     - Cantidad
     - CPUs
     - RAM
     - Núcleos Totales
   * - **Thin**
     - 83
     - 2 × Intel Xeon (12 cores)
     - 128 GB
     - 1,992
   * - **Semi Fat**
     - 40
     - 2 × Intel Xeon (12 cores)
     - 256 GB
     - 960

Infraestructura de Gestión
---------------------------

- **3 servidores de gestión:**
  
  - Servidor de login
  - Servidor de colas
  - Servidor de aprovisionamiento

----

Cluster Centepetl
===================================


--------------------------

:Arquitectura: Intel Xeon Phi Knights Landing
:Total de Núcleos: 3,060 núcleos de procesamiento
:Rendimiento: 135 TFlops
:Almacenamiento: 480 TB
:Red de Procesamiento: Intel Omnipath a100 Gbps

Nodos de Cálculo
-----------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1
   :align: center

   * - Cantidad
     - CPU
     - RAM por Nodo
     - Total Núcleos
   * - **45 nodos**
     - Intel Xeon Phi Knights Landing (68 cores)
     - 192 GB + 16 GB (208 GB)
     - 3,060

Características:
---------------------------

:Memoria de Alta Velocidad: 16 GB MCDRAM por nodo
:Red de Administración: Ethernet Gigabit
:Red de Procesamiento: Intel Omnipath 100 Gbps

Infraestructura de Gestión
---------------------------

- **2 servidores de gestión:**
  
  - Servidor de login
  - Servidor de aprovisionamiento

----

Cluster IBM Power9
===================================

Organizado en dos segmentos de 3 equipos cada uno.

------------------------------

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Componente
     - Especificación
   * - **Modelo**
     - IBM AC922 Power9
   * - **Procesadores**
     - 2 × Power9 de 20 cores
   * - **Memoria RAM**
     - 1,024 GB (1 TB)
   * - **Almacenamiento**
     - 2 × SSD SATA de 1.9 TB
   * - **GPUs**
     - 4 × NVIDIA Volta V100 SXM2 con NVLINK
   * - **Procesamiento Tensorial**
     - 125 TF Tensor Core para IA (por tarjeta)

Configuración del Cluster
--------------------------

:Total de Servidores: 6 servidores IBM AC922
:Total de GPUs: 24 NVIDIA Volta V100
:Rendimiento IA: 3 PetaFlops (FP16)
:Conexión: Incorporado al Storage Distribuido


----

Cluster Huapáctic
===================================

Cluster híbrido con nodos de cálculo y servidores especializados con GPU.

--------------------------

:Sistema Operativo: Rocky Linux 8.7 (Green Obsidian)
:Total de Núcleos CPU: 2,112 núcleos de procesamiento
:Total de GPUs: 16 NVIDIA Ampere A100

Nodos de Cálculo Tradicionales
-------------------------------

.. list-table::
   :widths: 20 15 20 20 25
   :header-rows: 1
   :align: center

   * - Tipo
     - Cantidad
     - CPUs
     - RAM
     - Núcleos Totales
   * - **Thin**
     - 84
     - 2 × Intel (12 cores)
     - 128 GB
     - 2,016
   * - **Fat**
     - 2
     - 2 × Intel (12 cores)
     - 256 GB
     - 48

Servidores con GPU
------------------

**4 Servidores Lenovo SR-670**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Componente
     - Especificación
   * - **Procesadores**
     - 2 × Intel Xeon Gold 6342 (24 cores @ 2.8 GHz)
   * - **Memoria RAM**
     - 1,024 GB (1 TB)
   * - **Almacenamiento NVMe**
     - 4 × NVMe PCIe 3.0 U.2 de 7.689 TB
   * - **Sistema Operativo**
     - 2 × U.2 NVMe PCIe 4.0 de 1.6 TB (RAID 1)
   * - **GPUs**
     - 4 × NVIDIA Ampere A100 SXM4 (80 GB RAM c/u)
   * - **Procesamiento Tensorial**
     - 312 TF (FP32) | 624 TF (FP16) por tarjeta
   * - **Interconexión GPU**
     - NVLINK

:Conexión: Incorporados al Storage Distribuido

----

Cluster Leviatán
===================================


--------------------------
-----------------------

:CPU: Intel(R) Xeon(R) E5-2680 v3 @ 2.50GHz
   - 24 hilos de procesamiento
   - Arquitectura Haswell

:Memoria RAM: 125 GiB

:Interfaz de Red: InfiniBand Mellanox ConnectX-3

:Sistema Operativo: Rocky Linux 9.6
   - Distribución empresarial compatible con RHEL
   - Optimizado para HPC

----

Particiones del Cluster
===================================


.. list-table:: 
   :widths: 15 10 45 15 15
   :header-rows: 1
   :align: center

   * - Partición
     - Nodos
     - Descripción
     - Características
     - Estado
   * - **normal**
     - 35
     - Cómputo general de propósito múltiple
     - Nodos C01-C38
     - Activo
   * - **fatcpu**
     - 40
     - Procesamiento con alta demanda de memoria
     - RAM extendida
     - Activo
   * - **gpu**
     - 2
     - Cómputo acelerado por GPU
     - Ampere/L402
     - Activo


----

Nodos de Cálculo Tradicionales
-------------------------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1
   :align: center

   * - Cantidad
     - CPUs
     - RAM
     - Núcleos Totales
   * - **40 nodos Thin**
     - 2 × Intel (12 cores)
     - 128 GB
     - 960

Servidor GPU - Configuración 1
-------------------------------

**1 Servidor Lenovo SR-670**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Componente
     - Especificación
   * - **Procesadores**
     - 2 × Intel Xeon Gold 6342 (24 cores @ 2.8 GHz)
   * - **Memoria RAM**
     - 1,024 GB (1 TB)
   * - **Almacenamiento NVMe**
     - 4 × NVMe PCIe 3.0 U.2 de 7.689 TB
   * - **Sistema Operativo**
     - 2 × U.2 NVMe PCIe 4.0 de 1.6 TB (RAID 1)
   * - **GPUs**
     - 4 × NVIDIA Ampere A100 SXM4 (80 GB RAM c/u)
   * - **Procesamiento Tensorial**
     - 312 TF (FP32) | 624 TF (FP16) por tarjeta
   * - **Interconexión GPU**
     - NVLINK

Servidor GPU - Configuración 2
-------------------------------

**1 Servidor Lenovo SR-670v2**

.. list-table::
   :widths: 30 70
   :header-rows: 1

   * - Componente
     - Especificación
   * - **Procesadores**
     - 2 × Intel Xeon Gold 6342 (24 cores @ 2.8 GHz)
   * - **Memoria RAM**
     - 1,024 GB (1 TB)
   * - **Sistema Operativo**
     - 2 × U.2 NVMe PCIe 4.0 de 1 TB (RAID 1)
   * - **GPUs**
     - 8 × NVIDIA Ampere L40
   * - **Procesamiento Tensorial**
     - 312 TF (FP32) | 624 TF (FP16) por tarjeta

:Conexión: Incorporados al Storage Distribuido

Almacenamiento Local
--------------------

:Sistema NVMe: All Flash NVMe de 110 TB útiles
:Tipo: Almacenamiento de alto rendimiento
:Uso: Datos temporales y procesamiento intensivo de E/S

----

Redes de Comunicación
===================================


------------

.. list-table::
   :widths: 25 25 25 25
   :header-rows: 1

   * - Red
     - Velocidad
     - Uso
     - Clusters
   * - **Ethernet Gigabit**
     - 1 Gbps
     - Gestión y aprovisionamiento
     - Todos
   * - **Infiniband FDR**
     - 56 Gbps
     - Comunicación entre nodos
     - Cuetlaxcoapan
   * - **Intel Omnipath**
     - 100 Gbps
     - Comunicación entre nodos
     - Centepetl
   * - **Enlace Internet**
     - 10 Gbps (dual)
     - Conectividad externa
     - Campus y Internet

Características de la Red
--------------------------

:Red de Gestión: Ethernet Gigabit para administración del hardware y aprovisionamiento de software
:Red de Procesamiento: Infiniband/Omnipath para comunicación de baja latencia
:Conectividad Externa: Enlace dual de 10 Gbps hacia campus del consorcio e Internet

----

Almacenamiento Global
===================================

Sistema de almacenamiento distribuido de alta capacidad y rendimiento.

Sistemas de Almacenamiento
---------------------------

.. list-table::
   :widths: 30 20 20 30
   :header-rows: 1

   * - Sistema
     - Capacidad Útil
     - Tecnología
     - Características
   * - **SAN RAID 6**
     - 360 TB
     - Cabinas con Infiniband 56 Gbps
     - Almacenamiento principal
   * - **All Flash NVMe**
     - 110 TB
     - NVMe de alta velocidad
     - Cluster Leviatán
   * - **Librería de Cintas**
     - 450 TB (1,125 TB comprimido)
     - LTO-7
     - Respaldo y archivo

Detalles por Sistema
---------------------

**Sistema SAN**
   :Arquitectura: Storage Area Network con RAID 6
   :Capacidad: 360 TB útiles
   :Conectividad: Infiniband a 56 Gbps
   :Uso: Almacenamiento compartido principal

**Sistema All Flash**
   :Tecnología: NVMe de estado sólido
   :Capacidad: 110 TB útiles
   :Cluster: Leviatán (uso exclusivo)
   :Rendimiento: Ultra bajo latencia, alto IOPS

**Librería de Cintas**
   :Tecnología: LTO-7 (Linear Tape-Open)
   :Capacidad sin compresión: 450 TB
   :Capacidad con compresión: Hasta 1,125 TB
   :Uso: Respaldo de largo plazo y archivo



Resumen de Capacidad Total
===================================

Capacidad de Procesamiento
---------------------------

.. list-table::
   :widths: 30 25 45
   :header-rows: 1

   * - Cluster
     - Núcleos CPU
     - Capacidad GPU
   * - **Cuetlaxcoapan**
     - 2,952
     - N/A
   * - **Centepetl**
     - 3,060
     - N/A
   * - **IBM Power9**
     - 240
     - 24 × NVIDIA Volta V100
   * - **Huapáctic**
     - 2,112
     - 16 × NVIDIA Ampere A100
   * - **Leviatán**
     - 960
     - 12 × NVIDIA Ampere (A100 + L40)
   * - **TOTAL**
     - **9,324 núcleos**
     - **52 GPUs**

Almacenamiento Total
--------------------

:Almacenamiento en Disco: 1,190 TB
:Almacenamiento en Cinta: 450 TB (1,125 TB comprimido)
:Total Combinado: 1,640 TB (1,765 TB con compresión)

----

Contacto
========

**Laboratorio Nacional de Supercómputo del Sureste de México**

:Ubicación: Boulevard Valsequillo, Ciudad Universitaria, Puebla
:Teléfono: +52 (222) 229 5500
:Correo: soporte-lns@cs.buap.mx
:Web: https://lns.buap.mx

**Benemérita Universidad Autónoma de Puebla**

:Dirección: 4 Sur 104, Centro Histórico, C.P. 72000
:Teléfono: +52 (222) 229 5500