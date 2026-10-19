import json
import shutil
from html import escape
from pathlib import Path

APP_NAME = "FencingNow - Scout & Stats"
SITE_URL = "https://fencingnow.app"
PLAY_URL = "https://play.google.com/store/apps/details?id=app.fencingnow.scout&pcampaignid=web_share"
STORE_URL = "https://apps.apple.com/br/app/fencingnow-scout-stats/id6798884700"
PRIVACY_BASE = "https://fencing-stats.github.io/fencing-stats-site/privacy.html"
OUTPUT_DIR = Path("docs")

LANGUAGES = {
    "en": {
        "path": "/", "directory": ".", "lang": "en", "hreflang": "en", "short": "EN", "name": "English",
        "title": "FencingNow - Scout & Stats | Fencing in the Digital Age",
        "description": "Record every bout, analyze performance and move your fencing forward with FencingNow - Scout & Stats.",
        "keywords": "fencing, fencing statistics, bout scouting, fencing analysis, scout stats",
        "nav_features": "Features", "nav_workflow": "How it works", "nav_languages": "Languages", "nav_download": "Download",
        "skip": "Skip to content", "menu": "Open navigation", "nav_label": "Primary navigation", "languages_label": "Languages",
        "presents": "FencingNow presents", "positioning": "Tools for Fencing in the Digital Age",
        "hero_copy": "lets you record every bout, analyze performance and move your fencing forward.",
        "hero_alt": "Two fencers competing on the piste with performance statistics", "weapons": "Foil · Épée · Sabre", "explore": "Explore",
        "the_app": "The app", "features_title_a": "Every action.", "features_title_b": "In context.",
        "features_intro": "Designed around the bout, from the first registered fencer to the final report.",
        "feature_1_label": "Bout scouting", "feature_1_title": "Keep the bout in focus.",
        "feature_1_copy": "Record the action as it happens across foil, épée and sabre, in bouts to 5 or 15 points.",
        "feature_2_label": "Touch timeline", "feature_2_title": "See the rhythm of the bout.", "feature_2_copy": "Register the touch timeline, action by action.",
        "feature_3_label": "Fencer profiles", "feature_3_title": "Start with the fencer.",
        "feature_3_copy": "Prepare each profile with name, handedness, age, nationality, club, ranking and notes.",
        "feature_4_label": "Analysis & reports", "feature_4_title": "Keep the information moving.",
        "feature_4_copy": "Build statistics and charts, review partial or final reports, export to PDF and access bout history.",
        "profile_ready": "Ready before the call", "stats": "Stats", "pdf": "PDF", "history": "History",
        "how": "How it works", "workflow_a": "From the piste to the", "workflow_b": "picture.",
        "step_1_title": "Set up the fencers.", "step_1_copy": "Register the fencers before the bout.",
        "step_2_title": "Record the bout.", "step_2_copy": "Register the bout as it develops on the piste.",
        "step_3_title": "Read the results.", "step_3_copy": "Review the recorded information after the final touch.",
        "community": "Built for the fencing community", "languages_a": "Speak the language of your", "languages_b": "piste.",
        "languages_copy": "FencingNow - Scout & Stats is available in five languages for your day-to-day work in fencing.",
        "device": "On your device", "download_a": "Ready when the bout", "download_b": "starts.",
        "download_copy": "Take FencingNow - Scout & Stats to your next bout.",
        "privacy": "Privacy Policy", "back_home": "Back to FencingNow home", "app_store_alt": "Download on the App Store", "play_store_alt": "Get it on Google Play",
        "privacy_hash": "en", "apple_badge": "app-store-en-us.svg", "play_badge": "google-play-en.png",
    },
    "pt": {
        "path": "/pt/", "directory": "pt", "lang": "pt-BR", "hreflang": "pt-BR", "short": "PT", "name": "Português",
        "title": "FencingNow - Scout & Stats | Esgrima na Era Digital",
        "description": "Registre cada assalto, analise o desempenho e faça sua esgrima evoluir com FencingNow - Scout & Stats.",
        "keywords": "esgrima, estatísticas de esgrima, scout de assaltos, análise de desempenho, esgrima digital",
        "nav_features": "Funcionalidades", "nav_workflow": "Como funciona", "nav_languages": "Idiomas", "nav_download": "Baixar",
        "skip": "Ir para o conteúdo", "menu": "Abrir navegação", "nav_label": "Navegação principal", "languages_label": "Idiomas",
        "presents": "FencingNow apresenta", "positioning": "Ferramentas para a esgrima na Era Digital",
        "hero_copy": "permite registrar cada assalto, analisar o desempenho e evoluir sua esgrima.",
        "hero_alt": "Dois esgrimistas em assalto na pista com estatísticas de desempenho", "weapons": "Florete · Espada · Sabre", "explore": "Explorar",
        "the_app": "O aplicativo", "features_title_a": "Cada ação.", "features_title_b": "No contexto.",
        "features_intro": "Pensado para o assalto, do primeiro cadastro de esgrimista ao relatório final.",
        "feature_1_label": "Scout do assalto", "feature_1_title": "Mantenha o foco no assalto.",
        "feature_1_copy": "Registre a ação ao vivo em florete, espada e sabre, nos assaltos de 5 ou 15 pontos.",
        "feature_2_label": "Linha do toque", "feature_2_title": "Veja o ritmo do assalto.", "feature_2_copy": "Registre a linha do toque, ação por ação.",
        "feature_3_label": "Perfis de esgrimistas", "feature_3_title": "Tudo começa pelo esgrimista.",
        "feature_3_copy": "Prepare cada perfil com nome, lateralidade, idade, nacionalidade, clube, ranking e observações.",
        "feature_4_label": "Análise e relatórios", "feature_4_title": "Mantenha a informação em movimento.",
        "feature_4_copy": "Veja estatísticas e gráficos, consulte relatórios parciais ou finais, exporte em PDF e acesse o histórico de assaltos.",
        "profile_ready": "Pronto antes da chamada", "stats": "Estatísticas", "pdf": "PDF", "history": "Histórico",
        "how": "Como funciona", "workflow_a": "Da pista à", "workflow_b": "análise.",
        "step_1_title": "Cadastre os esgrimistas.", "step_1_copy": "Registre os esgrimistas antes do assalto.",
        "step_2_title": "Registre o assalto ao vivo.", "step_2_copy": "Acompanhe a ação conforme ela acontece na pista.",
        "step_3_title": "Analise os resultados.", "step_3_copy": "Revise as informações registradas após o toque final.",
        "community": "Feito para a comunidade da esgrima", "languages_a": "Use a linguagem da sua", "languages_b": "pista.",
        "languages_copy": "FencingNow - Scout & Stats está disponível em cinco idiomas para o seu trabalho diário na esgrima.",
        "device": "No seu dispositivo", "download_a": "Pronto quando o assalto", "download_b": "começa.",
        "download_copy": "Leve FencingNow - Scout & Stats para o seu próximo assalto.",
        "privacy": "Política de Privacidade", "back_home": "Voltar para a página do FencingNow", "app_store_alt": "Baixe na App Store", "play_store_alt": "Disponível no Google Play",
        "privacy_hash": "pt", "apple_badge": "app-store-pt-br.svg", "play_badge": "google-play-pt-br.png",
    },
    "es": {
        "path": "/es/", "directory": "es", "lang": "es", "hreflang": "es", "short": "ES", "name": "Español",
        "title": "FencingNow - Scout & Stats | Esgrima en la Era Digital",
        "description": "Registra cada asalto, analiza el rendimiento y mejora tu esgrima con FencingNow - Scout & Stats.",
        "keywords": "esgrima, estadísticas de esgrima, scout de asaltos, análisis de rendimiento, esgrima digital",
        "nav_features": "Funciones", "nav_workflow": "Cómo funciona", "nav_languages": "Idiomas", "nav_download": "Descargar",
        "skip": "Ir al contenido", "menu": "Abrir navegación", "nav_label": "Navegación principal", "languages_label": "Idiomas",
        "presents": "FencingNow presenta", "positioning": "Herramientas para la esgrima en la era digital",
        "hero_copy": "te permite registrar cada asalto, analizar el rendimiento y avanzar en tu esgrima.",
        "hero_alt": "Dos esgrimistas compiten en la pista con estadísticas de rendimiento", "weapons": "Florete · Espada · Sable", "explore": "Explorar",
        "the_app": "La aplicación", "features_title_a": "Cada acción.", "features_title_b": "En contexto.",
        "features_intro": "Diseñada para el asalto, desde el primer tirador registrado hasta el informe final.",
        "feature_1_label": "Registro del asalto", "feature_1_title": "Mantén el asalto en el centro.",
        "feature_1_copy": "Registra la acción en directo en florete, espada y sable, en asaltos a 5 o 15 tocados.",
        "feature_2_label": "Cronología de tocados", "feature_2_title": "Ve el ritmo del asalto.", "feature_2_copy": "Registra la cronología de tocados, acción por acción.",
        "feature_3_label": "Perfiles de tiradores", "feature_3_title": "Todo empieza con el tirador.",
        "feature_3_copy": "Prepara cada perfil con nombre, lateralidad, edad, nacionalidad, club, ranking y observaciones.",
        "feature_4_label": "Análisis e informes", "feature_4_title": "Mantén la información en movimiento.",
        "feature_4_copy": "Consulta estadísticas y gráficos, revisa informes parciales o finales, exporta a PDF y accede al historial de asaltos.",
        "profile_ready": "Listo antes de la llamada", "stats": "Estadísticas", "pdf": "PDF", "history": "Historial",
        "how": "Cómo funciona", "workflow_a": "De la pista a la", "workflow_b": "visión general.",
        "step_1_title": "Prepara a los tiradores.", "step_1_copy": "Registra a los tiradores antes del asalto.",
        "step_2_title": "Registra el asalto en directo.", "step_2_copy": "Sigue la acción mientras sucede en la pista.",
        "step_3_title": "Analiza los resultados.", "step_3_copy": "Revisa la información registrada después del tocado final.",
        "community": "Hecha para la comunidad de la esgrima", "languages_a": "Habla el idioma de tu", "languages_b": "pista.",
        "languages_copy": "FencingNow - Scout & Stats está disponible en cinco idiomas para tu trabajo diario en la esgrima.",
        "device": "En tu dispositivo", "download_a": "Lista cuando empieza", "download_b": "el asalto.",
        "download_copy": "Lleva FencingNow - Scout & Stats a tu próximo asalto.",
        "privacy": "Política de privacidad", "back_home": "Volver a la página de FencingNow", "app_store_alt": "Descárgalo en el App Store", "play_store_alt": "Disponible en Google Play",
        "privacy_hash": "es", "apple_badge": "app-store-es-es.svg", "play_badge": "google-play-es-419.png",
    },
    "fr": {
        "path": "/fr/", "directory": "fr", "lang": "fr", "hreflang": "fr", "short": "FR", "name": "Français",
        "title": "FencingNow - Scout & Stats | L'escrime à l'ère numérique",
        "description": "Enregistrez chaque assaut, analysez la performance et faites progresser votre escrime avec FencingNow - Scout & Stats.",
        "keywords": "escrime, statistiques d'escrime, suivi des assauts, analyse de performance, escrime numérique",
        "nav_features": "Fonctionnalités", "nav_workflow": "Fonctionnement", "nav_languages": "Langues", "nav_download": "Télécharger",
        "skip": "Aller au contenu", "menu": "Ouvrir la navigation", "nav_label": "Navigation principale", "languages_label": "Langues",
        "presents": "FencingNow présente", "positioning": "Des outils pour l'escrime à l'ère du numérique",
        "hero_copy": "vous permet d'enregistrer chaque assaut, d'analyser la performance et de faire progresser votre escrime.",
        "hero_alt": "Deux escrimeurs s'affrontent sur la piste avec des statistiques de performance", "weapons": "Fleuret · Épée · Sabre", "explore": "Explorer",
        "the_app": "L'application", "features_title_a": "Chaque action.", "features_title_b": "En contexte.",
        "features_intro": "Pensée autour de l'assaut, du premier tireur enregistré au rapport final.",
        "feature_1_label": "Suivi de l'assaut", "feature_1_title": "Gardez l'assaut au centre.",
        "feature_1_copy": "Enregistrez l'action en direct dans les trois armes, pour les assauts en 5 ou 15 touches.",
        "feature_2_label": "Chronologie des touches", "feature_2_title": "Voyez le rythme de l'assaut.", "feature_2_copy": "Enregistrez la chronologie des touches, action par action.",
        "feature_3_label": "Profils des tireurs", "feature_3_title": "Tout commence par le tireur.",
        "feature_3_copy": "Préparez chaque profil avec le nom, la latéralité, l'âge, la nationalité, le club, le classement et les observations.",
        "feature_4_label": "Analyses et rapports", "feature_4_title": "Gardez l'information en mouvement.",
        "feature_4_copy": "Consultez les statistiques et graphiques, les rapports partiels ou finaux, exportez en PDF et accédez à l'historique des assauts.",
        "profile_ready": "Prêt avant l'appel", "stats": "Statistiques", "pdf": "PDF", "history": "Historique",
        "how": "Fonctionnement", "workflow_a": "De la piste à", "workflow_b": "l'analyse.",
        "step_1_title": "Préparez les tireurs.", "step_1_copy": "Enregistrez les tireurs avant l'assaut.",
        "step_2_title": "Enregistrez l'assaut en direct.", "step_2_copy": "Suivez l'action pendant qu'elle se déroule sur la piste.",
        "step_3_title": "Analysez les résultats.", "step_3_copy": "Consultez les informations enregistrées après la touche finale.",
        "community": "Conçue pour la communauté de l'escrime", "languages_a": "La langue de votre", "languages_b": "piste.",
        "languages_copy": "FencingNow - Scout & Stats est disponible en cinq langues pour votre travail quotidien en escrime.",
        "device": "Sur votre appareil", "download_a": "Prêt quand l'assaut", "download_b": "commence.",
        "download_copy": "Emmenez FencingNow - Scout & Stats à votre prochain assaut.",
        "privacy": "Politique de confidentialité", "back_home": "Retour à la page FencingNow", "app_store_alt": "Télécharger dans l’App Store", "play_store_alt": "Disponible sur Google Play",
        "privacy_hash": "fr", "apple_badge": "app-store-fr-fr.svg", "play_badge": "google-play-fr.png",
    },
    "it": {
        "path": "/it/", "directory": "it", "lang": "it", "hreflang": "it", "short": "IT", "name": "Italiano",
        "title": "FencingNow - Scout & Stats | Scherma nell'Era Digitale",
        "description": "Registra ogni assalto, analizza la prestazione e fai crescere la tua scherma con FencingNow - Scout & Stats.",
        "keywords": "scherma, statistiche di scherma, scouting degli assalti, analisi della prestazione, scherma digitale",
        "nav_features": "Funzioni", "nav_workflow": "Come funziona", "nav_languages": "Lingue", "nav_download": "Scarica",
        "skip": "Vai al contenuto", "menu": "Apri navigazione", "nav_label": "Navigazione principale", "languages_label": "Lingue",
        "presents": "FencingNow presenta", "positioning": "Strumenti per la scherma nell'era digitale",
        "hero_copy": "ti permette di registrare ogni assalto, analizzare la prestazione e far crescere la tua scherma.",
        "hero_alt": "Due schermidori si affrontano in pedana con statistiche sulla prestazione", "weapons": "Fioretto · Spada · Sciabola", "explore": "Esplora",
        "the_app": "L'app", "features_title_a": "Ogni azione.", "features_title_b": "Nel contesto.",
        "features_intro": "Progettata intorno all'assalto, dal primo schermidore registrato al rapporto finale.",
        "feature_1_label": "Scouting dell'assalto", "feature_1_title": "Mantieni l'assalto al centro.",
        "feature_1_copy": "Registra l'azione in diretta in fioretto, spada e sciabola, negli assalti a 5 o 15 stoccate.",
        "feature_2_label": "Sequenza delle stoccate", "feature_2_title": "Vedi il ritmo dell'assalto.", "feature_2_copy": "Registra la sequenza delle stoccate, azione dopo azione.",
        "feature_3_label": "Profili degli schermidori", "feature_3_title": "Tutto parte dallo schermidore.",
        "feature_3_copy": "Prepara ogni profilo con nome, lateralità, età, nazionalità, club, ranking e osservazioni.",
        "feature_4_label": "Analisi e rapporti", "feature_4_title": "Tieni le informazioni in movimento.",
        "feature_4_copy": "Consulta statistiche e grafici, rivedi rapporti parziali o finali, esporta in PDF e accedi allo storico degli assalti.",
        "profile_ready": "Pronto prima dell'appello", "stats": "Statistiche", "pdf": "PDF", "history": "Storico",
        "how": "Come funziona", "workflow_a": "Dalla pedana", "workflow_b": "all'analisi.",
        "step_1_title": "Prepara gli schermidori.", "step_1_copy": "Registra gli schermidori prima dell'assalto.",
        "step_2_title": "Registra l'assalto in diretta.", "step_2_copy": "Segui l'azione mentre si svolge in pedana.",
        "step_3_title": "Analizza i risultati.", "step_3_copy": "Rivedi le informazioni registrate dopo la stoccata finale.",
        "community": "Pensata per la comunità della scherma", "languages_a": "Parla la lingua della tua", "languages_b": "pedana.",
        "languages_copy": "FencingNow - Scout & Stats è disponibile in cinque lingue per il tuo lavoro quotidiano nella scherma.",
        "device": "Sul tuo dispositivo", "download_a": "Pronto quando", "download_b": "inizia l'assalto.",
        "download_copy": "Porta FencingNow - Scout & Stats al tuo prossimo assalto.",
        "privacy": "Informativa sulla privacy", "back_home": "Torna alla pagina FencingNow", "app_store_alt": "Scarica dall’App Store", "play_store_alt": "Disponibile su Google Play",
        "privacy_hash": "it", "apple_badge": "app-store-it-it.svg", "play_badge": "google-play-it.png",
    },
}


def h(value: str) -> str:
    return escape(value, quote=True)


def alternate_links() -> str:
    links = [f'    <link rel="alternate" hreflang="{data["hreflang"]}" href="{SITE_URL}{data["path"]}">' for data in LANGUAGES.values()]
    links.append(f'    <link rel="alternate" hreflang="x-default" href="{SITE_URL}/">')
    return "\n".join(links)


def language_links(current: str) -> str:
    chunks = []
    for code, data in LANGUAGES.items():
        current_attr = ' aria-current="page"' if code == current else ''
        chunks.append(f'<a href="{data["path"]}" lang="{data["lang"]}"{current_attr}>{data["short"]}</a>')
    return '<span aria-hidden="true">·</span>'.join(chunks)


def page(data: dict, code: str) -> str:
    return f'''<!doctype html>
<html lang="{h(data["lang"])}">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{h(data["title"])}</title>
    <meta name="description" content="{h(data["description"])}">
    <meta name="keywords" content="{h(data["keywords"])}">
    <meta name="theme-color" content="#050b18">
    <link rel="canonical" href="{SITE_URL}{data["path"]}">
{alternate_links()}
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="FencingNow">
    <meta property="og:title" content="{h(data["title"])}">
    <meta property="og:description" content="{h(data["description"])}">
    <meta property="og:url" content="{SITE_URL}{data["path"]}">
    <meta property="og:image" content="{SITE_URL}/assets/hero-fencingnow.png">
    <meta property="og:image:alt" content="{h(data["hero_alt"])}">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{h(data["title"])}">
    <meta name="twitter:description" content="{h(data["description"])}">
    <meta name="twitter:image" content="{SITE_URL}/assets/hero-fencingnow.png">
    <link rel="icon" href="/assets/fencingnow-favicon.png" type="image/png">
    <link rel="apple-touch-icon" href="/assets/fencingnow-favicon.png">
    <link rel="stylesheet" href="/styles.css">
  </head>
  <body>
    <a class="skip-link" href="#main-content">{h(data["skip"])}</a>

    <header class="site-header" data-header>
      <a class="brand" href="#top" aria-label="FencingNow">
        <span class="brand-mark"><img src="/assets/fencingnow-icon.webp" alt=""></span>
        <span class="brand-name">Fencing<span>Now</span></span>
      </a>
      <button class="menu-toggle" type="button" aria-expanded="false" aria-controls="primary-navigation">
        <span class="sr-only">{h(data["menu"])}</span><span></span><span></span>
      </button>
      <nav id="primary-navigation" class="primary-nav" aria-label="{h(data["nav_label"])}">
        <a href="#features">{h(data["nav_features"])}</a>
        <a href="#workflow">{h(data["nav_workflow"])}</a>
        <a href="#languages">{h(data["nav_languages"])}</a>
        <a href="#download" class="nav-download">{h(data["nav_download"])}</a>
        <div class="language-switcher" aria-label="{h(data["languages_label"])}">{language_links(code)}</div>
      </nav>
    </header>

    <main id="main-content" class="apps-catalogue">
      <article class="app-page">
        <section id="top" class="hero" aria-labelledby="hero-title">
          <div class="hero-image" role="img" aria-label="{h(data["hero_alt"])}"></div>
          <div class="hero-scanlines" aria-hidden="true"></div>
          <div class="hero-content page-shell">
            <p class="eyebrow"><span></span> {h(data["presents"])}</p>
            <h1 id="hero-title">Scout<br>Analyze<br><em>Improve</em></h1>
            <p class="hero-positioning">{h(data["positioning"])}</p>
            <p class="hero-copy"><strong>{h(APP_NAME)}</strong> {h(data["hero_copy"])}</p>
            <div class="store-actions" aria-label="{h(data["nav_download"])} {h(APP_NAME)}">
              <a class="store-badge" href="{STORE_URL}" target="_blank" rel="noopener noreferrer"><img src="/assets/badges/{data["apple_badge"]}" alt="{h(data["app_store_alt"])}"></a>
              <a class="store-badge hero-play-badge" href="{PLAY_URL}" target="_blank" rel="noopener noreferrer"><img src="/assets/badges/{data["play_badge"]}" alt="{h(data["play_store_alt"])}"></a>
            </div>
          </div>
          <div class="hero-status"><span class="status-dot"></span><span>{h(data["weapons"])}</span></div>
          <a class="scroll-cue" href="#features" aria-label="{h(data["explore"])}"><span></span><small>{h(data["explore"])}</small></a>
        </section>

        <section id="features" class="features section page-shell" aria-labelledby="features-title">
          <div class="section-intro stagger-reveal">
            <p class="eyebrow"><span></span> {h(data["the_app"])}</p>
            <h2 id="features-title">{h(data["features_title_a"])}<br><em>{h(data["features_title_b"])}</em></h2>
            <p>{h(data["features_intro"])}</p>
          </div>
          <div class="feature-layout">
            <article class="feature-card feature-card-large stagger-reveal"><div class="card-number">01</div><div class="card-icon icon-live" aria-hidden="true"><span></span><span></span><span></span></div><p class="card-label">{h(data["feature_1_label"])}</p><h3>{h(data["feature_1_title"])}</h3><p>{h(data["feature_1_copy"])}</p><div class="weapon-list"><span>{h(data["weapons"])}</span></div><div class="piste-line" aria-hidden="true"><span></span><i></i><b></b><i></i><span></span></div></article>
            <article class="feature-card feature-card-timeline stagger-reveal"><div class="card-number">02</div><div class="card-icon icon-timeline" aria-hidden="true"><span></span><span></span><span></span><span></span></div><p class="card-label">{h(data["feature_2_label"])}</p><h3>{h(data["feature_2_title"])}</h3><p>{h(data["feature_2_copy"])}</p><div class="timeline-demo" aria-hidden="true"><span class="blue"></span><span></span><span class="blue"></span><span class="cyan"></span><span></span><span class="cyan"></span><span></span></div></article>
            <article class="feature-card feature-card-fencer stagger-reveal"><div class="card-number">03</div><div class="fencer-data" aria-hidden="true"><div class="data-avatar">FN</div><div><b>{h(data["feature_3_label"])}</b><span>{h(data["profile_ready"])}</span></div></div><p class="card-label">{h(data["feature_3_label"])}</p><h3>{h(data["feature_3_title"])}</h3><p>{h(data["feature_3_copy"])}</p></article>
            <article class="feature-card feature-card-report stagger-reveal"><div class="card-number">04</div><div class="report-bars" aria-hidden="true"><span></span><span></span><span></span><span></span><span></span><i></i></div><p class="card-label">{h(data["feature_4_label"])}</p><h3>{h(data["feature_4_title"])}</h3><p>{h(data["feature_4_copy"])}</p><div class="report-tags"><span>{h(data["stats"])}</span><span>{h(data["pdf"])}</span><span>{h(data["history"])}</span></div></article>
          </div>
        </section>

        <section id="workflow" class="workflow section" aria-labelledby="workflow-title"><div class="workflow-grid page-shell"><div class="workflow-title stagger-reveal"><p class="eyebrow"><span></span> {h(data["how"])}</p><h2 id="workflow-title">{h(data["workflow_a"])}<br><em>{h(data["workflow_b"])}</em></h2></div><ol class="steps-list"><li class="stagger-reveal"><span>01</span><div><h3>{h(data["step_1_title"])}</h3><p>{h(data["step_1_copy"])}</p></div></li><li class="stagger-reveal"><span>02</span><div><h3>{h(data["step_2_title"])}</h3><p>{h(data["step_2_copy"])}</p></div></li><li class="stagger-reveal"><span>03</span><div><h3>{h(data["step_3_title"])}</h3><p>{h(data["step_3_copy"])}</p></div></li></ol></div></section>

        <section id="languages" class="languages section page-shell" aria-labelledby="languages-title"><div class="language-copy stagger-reveal"><p class="eyebrow"><span></span> {h(data["community"])}</p><h2 id="languages-title">{h(data["languages_a"])}<br><em>{h(data["languages_b"])}</em></h2><p>{h(data["languages_copy"])}</p></div><div class="language-orbit stagger-reveal" aria-label="English, Português, Español, Français, Italiano"><span class="orbit-line orbit-one"></span><span class="orbit-line orbit-two"></span><b>EN</b><b>PT</b><b>ES</b><b>FR</b><b>IT</b><i></i></div></section>

        <section id="download" class="download-section" aria-labelledby="download-title"><div class="download-inner page-shell stagger-reveal"><div><p class="eyebrow"><span></span> {h(data["device"])}</p><h2 id="download-title">{h(data["download_a"])}<br><em>{h(data["download_b"])}</em></h2></div><div class="download-side"><p>{h(data["download_copy"])}</p><div class="store-actions"><a class="store-badge" href="{STORE_URL}" target="_blank" rel="noopener noreferrer"><img src="/assets/badges/{data["apple_badge"]}" alt="{h(data["app_store_alt"])}"></a><a class="store-badge" href="{PLAY_URL}" target="_blank" rel="noopener noreferrer"><img src="/assets/badges/{data["play_badge"]}" alt="{h(data["play_store_alt"])}"></a></div></div></div></section>
      </article>
    </main>

    <footer class="site-footer"><div class="page-shell footer-inner"><a class="brand" href="#top" aria-label="{h(data["back_home"])}"><span class="brand-mark"><img src="/assets/fencingnow-icon.webp" alt=""></span><span class="brand-name">Fencing<span>Now</span></span></a><div class="footer-links"><a href="{PRIVACY_BASE}#{data["privacy_hash"]}">{h(data["privacy"])}</a><a href="mailto:fencingstats1@gmail.com">fencingstats1@gmail.com</a><a href="https://www.instagram.com/fencingnow/" target="_blank" rel="noopener noreferrer">Instagram</a></div><p>© <span data-year></span> FencingNow</p></div></footer>
    <script src="/script.js"></script>
  </body>
</html>
'''


if OUTPUT_DIR.exists():
    shutil.rmtree(OUTPUT_DIR)
OUTPUT_DIR.mkdir()

for source in (
    "styles.css",
    "script.js",
    "assets/fencingnow-favicon.png",
    "assets/fencingnow-icon.webp",
    "assets/hero-fencingnow.png",
    "assets/hero-fencingnow.webp",
):
    destination = OUTPUT_DIR / source
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

for source in Path("assets/badges").glob("*"):
    destination = OUTPUT_DIR / source
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, destination)

for code, language in LANGUAGES.items():
    destination = OUTPUT_DIR / language["directory"] / "index.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page(language, code), encoding="utf-8")
    print(destination)

routes = [{"path": data["path"], "title": data["title"]} for data in LANGUAGES.values()]
Path(OUTPUT_DIR / "manus-routes.json").write_text(json.dumps({"routes": routes}, ensure_ascii=False) + "\n", encoding="utf-8")
Path(OUTPUT_DIR / "CNAME").write_text("fencingnow.app\n", encoding="utf-8")
Path(OUTPUT_DIR / ".nojekyll").touch()
Path(OUTPUT_DIR / "robots.txt").write_text("User-agent: *\nAllow: /\n\nSitemap: https://fencingnow.app/sitemap.xml\n", encoding="utf-8")

sitemap_entries = "\n".join(f"  <url><loc>{SITE_URL}{data['path']}</loc></url>" for data in LANGUAGES.values())
Path(OUTPUT_DIR / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{sitemap_entries}\n</urlset>\n', encoding="utf-8")
