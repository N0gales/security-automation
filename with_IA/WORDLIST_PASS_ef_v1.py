from pprint import pprint
from datetime import datetime
import os, re

# ==============================
# CONFIG
# ==============================

categorias = {
    "identidad_basica": ["nombre","apellido_1","apellido_2","apodo","iniciales","dia_nacimiento","mes_nacimiento","año_nacimiento","numero_favorito"],
    "vinculos_emocionales": ["nombre_pareja","nombres_hijos","años_nacimiento_hijos","nombre_mascota","apodo_mascota"],
    "localizacion": ["ciudad","barrio","pueblo_origen","pais"],
    "vida_profesional": ["empresa_actual","profesion"],
    "gustos_aficiones": ["equipo_futbol","cantante_favorito","grupo_musical","actor_favorito","serie_favorita","personaje_favorito"],
    "fechas_significativas": ["año_boda","año_relacion"],
    "cosas_cotidianas": ["marca_coche","modelo_coche","nombre_calle","numero_casa"]
}

SIMBOLOS = "!@#$%^&*()-_=+[]{};:,.<>?/|\\"
LEET = str.maketrans("aeios","43105")

# ==============================
# INPUT
# ==============================

def pedir(cat, campos):
    print(f"\n=== {cat.upper()} ===")
    d={}
    for c in campos:
        val = input(f"{c.replace('_',' ').capitalize()}: ")
        if val:
            d[c]=[x.strip() for x in val.split(",")] if "hijos" in c else val.strip()
    return d

def recolectar():
    datos = {}
    for c, campos in categorias.items():
        r = pedir(c, campos)   # ← se llama SOLO UNA VEZ
        if r:
            datos[c] = r

    año = datetime.now().year
    datos.setdefault("identidad_basica", {})["ultimos_5_años"] = [str(año - i) for i in range(6)]
    return datos

# ==============================
# BASES
# ==============================

def expandir(t):
    p=t.split()
    if len(p)==1: return {t}
    low=[x.lower() for x in p]; cap=[x.capitalize() for x in p]
    return {"".join(low),"".join(cap),cap[0]+"".join(low[1:]),"_".join(low),"-".join(low)}

def palabras(datos):
    vals=(v for cat in datos.values() for v in cat.values())
    flat=(i for v in vals for i in (v if isinstance(v,list) else [v]))
    return {w for f in flat for w in expandir(f)}

def numeros(datos):
    base={m for cat in datos.values() for v in cat.values()
          for m in re.findall(r'\d+'," ".join(v) if isinstance(v,list) else v)}
    ult=datos.get("identidad_basica",{}).get("ultimos_5_años",[])
    base|=set(ult)|{"123","1234","111","007","10"}
    out=set(base)
    for n in base:
        if len(n)==4: out.add(n[-2:])
        if len(set(n))==1: out|={n[0]*i for i in range(2,7)}
        if len(n)==2: out|={n*2,n+n[::-1]}
    return out

# ==============================
# GENERADOR
# ==============================

def generar(words, nums, minlen=6):
    res=set()
    for w in words:
        cap=w.capitalize(); base=w; leet=w.lower().translate(LEET)
        res.add(cap)
        for n in nums:
            res|={cap+n,base+n,n+cap,n+base}
            res|={cap+n+s for s in SIMBOLOS}
            res|={cap+s+n for s in SIMBOLOS}
            res|={n+cap+s for s in SIMBOLOS}
            res.add(leet.capitalize()+n+"!")
    res|={a.capitalize()+b.capitalize() for a in words for b in words if a!=b}
    res|={a.lower()+b.lower() for a in words for b in words if a!=b}
    res|={a+"_"+b for a in words for b in words if a!=b}
    res|={a+"-"+b for a in words for b in words if a!=b}
    return {r for r in res if len(r)>=minlen}

# ==============================
# GUARDAR
# ==============================

def guardar(wl):
    path=os.path.join(os.path.dirname(os.path.abspath(__file__)),"wordlist.txt")
    with open(path,"w",encoding="utf-8") as f: f.write("\n".join(sorted(wl)))
    print(f"\n📁 {len(wl)} contraseñas guardadas en {path}")

# ==============================
# MAIN
# ==============================

if __name__=="__main__":
    datos=recolectar()
    print("\n📦 DATOS:\n"); pprint(datos)
    wl=generar(palabras(datos),numeros(datos))
    guardar(wl)
    print("\n✅ Listo.")
