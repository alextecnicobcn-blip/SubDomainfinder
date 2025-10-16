#BY VENDETA. ENJOY.

import requests

# 🔐 Tu API key de SecurityTrails
API_KEY = "Tu API KEY"

def get_subdomains(domain):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"APIKEY": API_KEY}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subdomains = data.get("subdomains", [])
        return [f"{sub}.{domain}" for sub in subdomains]
    else:
        print(f"❌ Error al obtener subdominios: {response.status_code}")
        return []

def check_active(subdomain):
    for protocol in ["http://", "https://"]:
        try:
            response = requests.get(f"{protocol}{subdomain}", timeout=3)
            if response.status_code < 400:
                return True
        except requests.RequestException:
            continue
    return False

def main():
    domain = input("🔍 Introduce el dominio que quieres analizar (ej. ejemplo.com): ").strip()
    subdomains = get_subdomains(domain)

    print(f"🔎 Verificando subdominios activos...")
    active = [sub for sub in subdomains if check_active(sub)]

    print(f"\n✅ Subdominios activos encontrados ({len(active)}):")
    for sub in active:
        print(f"- {sub}")

    with open("subdominios_activos.txt", "w") as f:
        for sub in active:
            f.write(sub + "\n")
    print("\n📁 Resultados guardados en 'subdominios_activos.txt'")

if __name__ == "__main__":
    main()
