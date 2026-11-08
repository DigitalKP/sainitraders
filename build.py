import os, html
DOMAIN = "https://packagingtraders.in"
BASE = ""
OUT = os.path.dirname(os.path.abspath(__file__))
NAME = "SAINI TRADERS"
ADDR = "D-95, Ispat Nagar, Kanpur, Bhautipratappur, Uttar Pradesh 208022, India"
WA = "https://wa.me/919140948445"
WA_MSG = WA + "?text=Hello%20SAINI%20TRADERS%2C%20I%20need%20stretch%20film.%20Please%20share%20details."
GBP = "https://share.google/VzrvVFiXEuR6slk6Q"
DIR = "https://www.google.com/maps/dir/?api=1&destination=D-95%2C+Ispat+Nagar%2C+Kanpur%2C+Uttar+Pradesh+208022"
EMBED = "https://www.google.com/maps?q=D-95+Ispat+Nagar+Kanpur+Uttar+Pradesh+208022&output=embed"
PARENT = "/stretch-film-supplier-near-me/"

CSS = """:root{--n:#0b2447;--n2:#16365f;--g:#d4a72c;--bg:#fff;--s:#f3f6fa;--t:#1b2433;--m:#55627a;--l:#dbe3ee;--link:#0b57d0;--link-h:#0842a0}
@media(prefers-color-scheme:dark){:root{--bg:#0a1424;--s:#102038;--t:#e8eef8;--m:#a9b7cc;--l:#223555;--n:#e8eef8;--n2:#cfdcf0;--link:#ffd166;--link-h:#ffe08a}.hero,.cta{--n:#0b2447;--n2:#16365f}}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font:17px/1.65 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;color:var(--t);background:var(--bg)}
a{color:var(--link)}.w{max-width:1080px;margin:0 auto;padding:0 20px}
main a:not(.btn),.crumb a,footer a{color:var(--link);font-weight:600;text-decoration:underline;text-underline-offset:3px}
main a:not(.btn):hover,.crumb a:hover,footer a:hover{color:var(--link-h)}
.cta p a{color:#ffd166;font-weight:700;text-decoration:underline;text-underline-offset:3px}
header{border-bottom:1px solid var(--l);position:sticky;top:0;background:var(--bg);z-index:5}
.bar{display:flex;align-items:center;justify-content:space-between;gap:12px;min-height:64px;flex-wrap:wrap}
.logo{display:flex;align-items:center;gap:10px;font-weight:800;letter-spacing:.02em;text-decoration:none;color:var(--n)}.logo b{color:var(--g)}
nav a{margin-left:16px;text-decoration:none;font-size:15px;color:var(--m);font-weight:600}nav a:hover{color:var(--link)}
.btn{display:inline-block;padding:12px 22px;border-radius:6px;background:var(--g);color:#0b2447;font-weight:700;text-decoration:none;border:2px solid var(--g)}
.btn.o{background:transparent;color:#fff;border-color:#fff}.btn:focus-visible,a:focus-visible{outline:3px solid var(--g);outline-offset:2px}
.hero{background:var(--n2);background:linear-gradient(135deg,#0b2447,#16365f);color:#fff;padding:48px 0}
.hero .w{display:grid;gap:32px;grid-template-columns:1.3fr 1fr;align-items:center}
.hero h1{font-size:clamp(28px,4.5vw,44px);line-height:1.15;margin:0 0 14px}.hero p{color:#d6e0f0;margin:0 0 22px}
.hero .btn{margin:0 10px 10px 0}
.crumb{font-size:14px;padding:12px 0;color:var(--m)}
h2{font-size:clamp(22px,3vw,30px);line-height:1.25;color:var(--n);margin:40px 0 12px}h3{font-size:19px;margin:0 0 6px;color:var(--n)}
main p{max-width:72ch}.grid{display:grid;gap:16px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.card{border:1px solid var(--l);border-left:4px solid var(--g);border-radius:6px;padding:16px 18px;background:var(--s)}.card p{margin:0;font-size:15.5px;color:var(--m)}
.loc{border-bottom:1px solid var(--l);padding:14px 0}.loc p{margin:0}
details{border:1px solid var(--l);border-radius:6px;padding:12px 16px;margin:10px 0;background:var(--s)}summary{cursor:pointer;font-weight:600;color:var(--n)}
.map{width:100%;height:320px;border:0;border-radius:6px}
.cta{background:#0b2447;color:#fff;padding:36px 0;margin-top:48px}.cta h2{color:#fff;margin-top:0}.cta p{color:#d6e0f0}
footer{padding:28px 0;font-size:14px;color:var(--m);border-top:1px solid var(--l)}footer a{margin-right:12px}
.fab{position:fixed;right:16px;bottom:16px;z-index:6;box-shadow:0 4px 14px rgba(0,0,0,.25)}
.logo img{border-radius:8px;display:block}.hero img{width:100%;height:auto;border-radius:8px;display:block}.pic{float:right;margin:0 0 12px 20px;width:240px;max-width:42%}.pic img{width:100%;height:auto;border-radius:8px;display:block}
.trust-bar{background:var(--s);border:1px solid var(--l);border-left:4px solid var(--g);padding:14px 18px;border-radius:6px;margin:20px 0;font-weight:600}
.tbl-wrap{overflow-x:auto;margin:18px 0}
table.cmp{width:100%;border-collapse:collapse;background:var(--s);border:1px solid var(--l);border-radius:6px;overflow:hidden}
table.cmp th,table.cmp td{padding:12px 16px;text-align:left;border-bottom:1px solid var(--l)}
table.cmp th{background:#0b2447;color:#fff;font-weight:700}
table.cmp td:nth-child(2){font-weight:600;color:var(--n)}
.feat-img{margin:24px 0;border:1px solid var(--l);border-radius:8px;overflow:hidden;background:var(--s);max-width:720px}
.feat-img img{width:100%;height:auto;display:block}
.feat-img figcaption{padding:10px 16px;font-size:14.5px;color:var(--m)}
ul.clean,ol.clean{padding-left:22px;max-width:72ch}ul.clean li,ol.clean li{margin-bottom:8px}
@media(max-width:760px){.pic{float:none;margin:0 0 14px;max-width:100%;width:100%}.hero .w{grid-template-columns:1fr}nav a{margin:0 12px 0 0}.bar{padding:8px 0}}
@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}"""

ROLL = f'<img src="{BASE}/assets/stretch-film-pallet-hero.webp" width="720" height="523" alt="Transparent stretch film rolls stacked on a pallet" fetchpriority="high" decoding="async">' 

DADA_NAGAR_FAQS = [
 ("Dada Nagar mein stretch film kahan milegi?", "Saini Traders Dada Nagar Chauraha ke paas hai. Call, WhatsApp ya seedha visit karo. Factory tak delivery bhi hoti hai."),
 ("Where can I find the lowest cost stretch film supplier near Dada Nagar Chauraha?", "We supply direct from local stock, so you avoid freight and dealer margins. Share micron and quantity on 09140948445 for our best wholesale rate."),
 ("Where can I find a stretch film dealer close to me in Dada Nagar?", "We are near Dada Nagar Chauraha and Coca Cola Chauraha, close to the SBI Bank branch by the Police Station. Share your location and we will confirm the fastest delivery."),
 ("Do you provide same-day urgent delivery to factories near Coca Cola Chauraha?", "Yes. Orders confirmed before 5:00 PM are dispatched the same day, subject to stock. For emergencies, call directly on 09140948445."),
 ("What is your bulk pricing structure and minimum order?", "Rates depend on micron, weight and quantity, and improve with volume. Both single-roll and bulk cartoon/pallet orders are welcome. Regular buyers can ask for a monthly rate."),
 ("How do you guarantee roll weight and micron consistency?", "Net and core weight are declared, and you can weigh at delivery. We supply the micron you order. If a roll does not match, we provide hassle-free replacement."),
 ("Do you give credit to regular factories?", "Yes, for established units after a trial order and verification. Call 09140948445 to discuss."),
 ("Can I pick up the material myself?", "Yes. We are near the SBI Bank branch by the Police Station. Call before coming so your order is ready."),
]

LOCS = [
 dict(slug="kanpur", name="Kanpur", h1="Stretch Film Supplier in Kanpur", title="Stretch Film Supplier in Kanpur | SAINI TRADERS", desc="Enquire about hand-grade and machine-grade stretch film rolls in Kanpur from SAINI TRADERS, Ispat Nagar. Call or WhatsApp for requirements.",
  para="Kanpur has long been a city of manufacturing, leather, textiles, chemicals and trading, and almost every one of those businesses ends the day by wrapping goods for dispatch. Our base in Ispat Nagar is within the city itself, so businesses across Kanpur can enquire about stretch film rolls without looking outside town. Our {link} page covers the grades we handle and how to enquire.",
  intro="SAINI TRADERS is a packaging company located in Ispat Nagar, Kanpur. If your business is anywhere in the city and you are looking for stretch film rolls, this is the page to start with. We handle hand-grade and machine-grade stretch film in transparent and black variants, for single-roll and bulk requirements.",
  h2="What Kanpur businesses usually wrap", focus="Kanpur's mix of factories, godowns, wholesale markets and transport operators means stretch film is used on very different loads: cartons stacked on pallets, bagged material, boxed electricals, rolled fabric, drums and loose machine parts. Hand-grade rolls suit small and medium dispatch volumes, while machine-grade rolls suit businesses that wrap a steady number of pallets every day.",
  tip="Tell us what you pack, the pallet size and how many pallets you wrap in a typical week. That is usually enough for us to suggest a suitable grade and roll size.",
  faqs=[("Where is SAINI TRADERS located in Kanpur?","Our address is D-95, Ispat Nagar, Kanpur, Bhautipratappur, Uttar Pradesh 208022. The directions button on this page opens it in Google Maps."),("Can I buy a single roll?","Yes, single-roll enquiries are welcome, as well as bulk requirements. Contact us on WhatsApp with your requirement.")],
  near=["panki","fazalganj"]),
 dict(slug="panki", name="Panki", h1="Stretch Film Supplier Near Panki, Kanpur", title="Stretch Film Supplier Near Panki, Kanpur | SAINI TRADERS", desc="Looking for stretch film near Panki, Kanpur? SAINI TRADERS offers hand and machine grade stretch film rolls for industrial packaging. Enquire today.",
  para="Panki is one of Kanpur's established industrial belts, with factories that dispatch finished goods on pallets every day. Businesses searching for a stretch film supplier near Panki can enquire with us about hand-grade and machine-grade rolls for pallet wrapping and load stabilising. Our {link} page has more detail for this area.",
  intro="Panki is known for its factories and the steady movement of goods in and out of them. Units here often need stretch film in regular quantities, and a supplier they can reach by phone or WhatsApp rather than chasing through a long chain of middlemen. SAINI TRADERS serves enquiries from Panki with stretch film rolls for packaging and pallet wrapping.",
  h2="Stretch film for factory dispatch near Panki", focus="For production units, the choice often comes down to volume. A unit wrapping a handful of pallets a day can work well with hand-grade rolls, while a unit with a dedicated wrapping station will usually prefer machine-grade film, which is made for use on a wrapping machine and a steady, repeatable wrap. Black stretch film is also used where contents should not be visible during transit.",
  tip="If you already run a pallet wrapping machine, share its roll core size and the film width you use so we can match your requirement.",
  faqs=[("Do you have a shop in Panki?","No. Our only address is D-95, Ispat Nagar, Kanpur. We take enquiries from Panki by phone and WhatsApp."),("Which film is better for a wrapping machine?","Machine-grade stretch film is designed for that purpose. Share your machine details and we will help you pick."),],
  near=["dada-nagar","kanpur"]),
 dict(slug="dada-nagar", name="Dada Nagar",
  h1="Stretch Film Supplier in Dada Nagar, Kanpur: Direct Wholesale Rate, Same-Day Delivery",
  title="Stretch Film Supplier in Dada Nagar, Kanpur | Direct Wholesale Rate | Saini Traders",
  desc="Nearby stretch film supplier at Dada Nagar Chauraha & Coca Cola Chauraha. Exact micron, proper roll weight, same-day delivery. Rated 5★ by local buyers. Call for today’s rate.",
  custom_lead="Dispatch ruka hua hai? Stock khatam? Ek call karo, maal ghanton mein factory gate par.",
  para="Dada Nagar is home to a dense cluster of small and mid-sized manufacturing units, many of which pack goods by hand and move them out in modest, frequent batches. If you run such a unit and want a stretch film supplier in Dada Nagar with direct wholesale rate and same-day delivery, check our {link} page.",
  intro="", h2="", focus="", tip="",
  faqs=DADA_NAGAR_FAQS,
  near=["panki","fazalganj","ratan-lal-nagar","kanpur"]),
 dict(slug="ratan-lal-nagar", name="Ratan Lal Nagar", h1="Stretch Film Supplier Near Ratan Lal Nagar, Kanpur", title="Stretch Film Supplier Near Ratan Lal Nagar, Kanpur | SAINI TRADERS", desc="Stretch film rolls for businesses near Ratan Lal Nagar, Kanpur. Transparent and black, hand and machine grade. Contact SAINI TRADERS.",
  para="Ratan Lal Nagar combines workshops, small factories and trading establishments, so packaging needs here range from a few cartons to full pallet loads. Anyone looking for a stretch film supplier near Ratan Lal Nagar can read our {link} page and then reach out with their requirement.",
  intro="Ratan Lal Nagar is a busy mixed-use part of Kanpur, where small manufacturers, traders and service businesses operate side by side. Packaging requirements here are varied, which is why we keep both hand-grade and machine-grade stretch film in the conversation from the start.",
  h2="Mixed packaging needs, one supplier", focus="A trader sending bundled stock to another city, a workshop wrapping finished parts, and a small manufacturer sending pallets to a distributor all use stretch film differently. We help you match the film to the job: transparent film when staff need to identify contents at a glance, and black film when privacy or light protection matters.",
  tip="If your goods are sharp-edged or heavy, tell us. That can influence the film grade and how many wraps are sensible.",
  faqs=[("Can I get both transparent and black film?","Yes. Both are part of our range, in hand-grade and machine-grade options."),("Do you list prices online?","No. Stretch film requirements vary, so we respond to enquiries individually.")],
  near=["dada-nagar","kidwai-nagar"]),
 dict(slug="kidwai-nagar", name="Kidwai Nagar", h1="Stretch Film Supplier Near Kidwai Nagar, Kanpur", title="Stretch Film Supplier Near Kidwai Nagar, Kanpur | SAINI TRADERS", desc="Enquire for stretch film near Kidwai Nagar, Kanpur. SAINI TRADERS supplies hand and machine grade rolls for warehouses, traders and shippers.",
  para="Kidwai Nagar has a strong commercial character, with shops, distributors and storage spaces that regularly repack and forward goods. Businesses here looking for a stretch film supplier near Kidwai Nagar can see what we handle on our {link} page, covering both single rolls and larger quantities.",
  intro="Kidwai Nagar is a well-known commercial part of Kanpur, and trading and distribution are a big part of daily activity. For these businesses, stretch film is a routine consumable: it secures cartons on pallets, bundles loose items and protects parcels while they wait for transport.",
  h2="Stretch film for distributors and storage", focus="Distributors tend to value consistency: the same film, reorder after reorder. If your stock moves through warehouses and onto goods carriers, a reliably clinging transparent film helps keep loads stable and lets you scan labels without unwrapping. For repackaged consumer goods, hand-grade rolls in smaller quantities are common.",
  tip="Let us know how often you reorder. We can discuss whether single rolls or bulk quantities make more sense for you.",
  faqs=[("Is bulk supply available for traders?","Bulk requirements are welcome. Share your quantity and we will respond to your enquiry."),("Can I visit before ordering?","You are welcome to visit our Ispat Nagar address during business hours, 9:00 AM to 8:00 PM, every day.")],
  near=["ratan-lal-nagar","shastri-nagar"]),
 dict(slug="fazalganj", name="Fazalganj", h1="Stretch Film Supplier Near Fazalganj, Kanpur", title="Stretch Film Supplier Near Fazalganj, Kanpur | SAINI TRADERS", desc="Industrial stretch film supplier for Fazalganj, Kanpur. Hand and machine grade rolls for pallet wrapping and heavy goods. Call SAINI TRADERS.",
  para="Fazalganj is an industrial area where metal parts, machinery and heavy consignments are a common sight. For businesses here, a stretch film supplier near Fazalganj needs to understand heavier, awkward loads. Our {link} page explains the options we handle.",
  intro="Fazalganj has a long manufacturing tradition, and many units here pack heavier or more awkward goods than a typical carton warehouse: components, castings, drums and machinery parts. Stretch film cannot replace strapping on the heaviest loads, but it is widely used to hold items together and keep dust and moisture splashes off them.",
  h2="Film choices for heavier loads", focus="Heavier loads generally call for more wraps and a film that holds tension well. Machine-grade film is often chosen where a wrapping machine applies consistent tension. Black film is sometimes preferred for parts where protection from light or concealing contents is useful. Tell us what you wrap, and we can talk through the best fit.",
  tip="Share the approximate weight and shape of a typical load so we can discuss suitable film and wrapping practice.",
  faqs=[("Can stretch film replace strapping?","For very heavy loads, film is usually used together with strapping or other securing. It holds items together and protects them."),("Which film suits metal parts?","It depends on the weight and shape. Contact us with details and we will advise.")],
  near=["kanpur","shastri-nagar"]),
 dict(slug="shastri-nagar", name="Shastri Nagar", h1="Stretch Film Supplier Near Shastri Nagar, Kanpur", title="Stretch Film Supplier Near Shastri Nagar, Kanpur | SAINI TRADERS", desc="Stretch film rolls near Shastri Nagar, Kanpur for shops, home-based businesses and small traders. Enquire with SAINI TRADERS on call or WhatsApp.",
  para="Shastri Nagar is largely residential and commercial, where home-based sellers, small shops and local service providers often need a few rolls of stretch film at a time. If that describes you, our {link} page explains how single-roll enquiries work.",
  intro="Not every stretch film buyer runs a factory. In neighbourhoods like Shastri Nagar, many customers are small shopkeepers, online sellers working from home, and people who need to wrap furniture or household goods before a move. Hand-grade stretch film is the practical choice for all of them.",
  h2="Single rolls for small businesses and moving", focus="Hand-grade rolls are easy to use without any machine, and a single roll goes a long way for parcel bundling, wrapping furniture and keeping stock tidy on shelves. If your business is growing, we can also talk through larger quantities when the time comes.",
  tip="Mention what you want to wrap, such as furniture, cartons or appliances, and we will suggest a suitable roll.",
  faqs=[("Do you sell small quantities?","Yes, single-roll enquiries are welcome."),("Is film suitable for wrapping furniture?","Yes, hand-grade film is commonly used for protecting furniture from dust and scratches while moving.")],
  near=["kidwai-nagar","kanpur"]),
 dict(slug="unnao", name="Unnao", h1="Stretch Film Supplier in Unnao", title="Stretch Film Supplier in Unnao | SAINI TRADERS, Kanpur", desc="Stretch film enquiries from Unnao handled by SAINI TRADERS, Kanpur. Hand-grade and machine-grade rolls for industrial packaging and logistics.",
  para="Unnao sits next to Kanpur and has its own industrial and trading activity, with many businesses already working with suppliers in Kanpur. If you are in Unnao and need stretch film, read our {link} page. Please note that our address is in Kanpur, and we discuss delivery arrangements individually.",
  intro="Unnao is a separate district neighbouring Kanpur, with its own factories, godowns and traders. SAINI TRADERS operates from Ispat Nagar, Kanpur, and we welcome stretch film enquiries from Unnao businesses. We do not have an office in Unnao.",
  h2="Enquiries from Unnao", focus="Because we are based in Kanpur, the best way to start is a call or WhatsApp message with your requirement: the film grade you use, the roll quantity and your location. We will respond with what we can offer and discuss any logistics directly, so there are no assumptions on either side.",
  tip="Include your area in Unnao and your expected quantity in your first message to speed up the conversation.",
  faqs=[("Do you have an office in Unnao?","No. Our only address is D-95, Ispat Nagar, Kanpur."),("Can you deliver to Unnao?","Delivery depends on the order and is discussed per enquiry. Please contact us for details.")],
  near=["kanpur","panki"]),
]
BY={l["slug"]:l for l in LOCS}
def url(s): return f"/stretch-film-supplier-in-{s}/"

FAQ_PARENT=[("What is stretch film used for?","It is a stretchable plastic film wrapped around goods or pallets to hold them together and protect them from dust and handling during storage and transport."),
("What is the difference between hand-grade and machine-grade stretch film?","Hand-grade rolls are meant to be applied manually. Machine-grade rolls are designed for pallet wrapping machines and consistent, repeatable wrapping."),
("Do you supply single rolls as well as bulk?","Yes. Both single-roll and bulk requirements are welcome."),
("How can I get a quote?","Message us on WhatsApp or call 09140948445 or 07786843061. We discuss requirements individually, so no prices are listed on this website.")]

import json

def schema(trail, faqs=None):
    graph = [{
        "@type": "LocalBusiness",
        "@id": f"{DOMAIN}/#business",
        "name": "Saini Traders",
        "description": "Packaging company in Kanpur supplying hand-grade and machine-grade stretch film rolls.",
        "url": f"{DOMAIN}/",
        "logo": f"{DOMAIN}/assets/logo.webp",
        "image": f"{DOMAIN}/assets/stretch-film-pallet-hero.webp",
        "telephone": "+91-9140948445",
        "priceRange": "₹₹",
        "hasMap": GBP,
        "sameAs": [GBP],
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "D-95, Ispat Nagar, Bhautipratappur",
            "addressLocality": "Kanpur",
            "addressRegion": "Uttar Pradesh",
            "postalCode": "208022",
            "addressCountry": "IN"
        },
        "geo": {
            "@type": "GeoCoordinates",
            "latitude": 26.4499,
            "longitude": 80.3319
        },
        "openingHoursSpecification": {
            "@type": "OpeningHoursSpecification",
            "dayOfWeek": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
            "opens": "09:00",
            "closes": "20:00"
        }
    }]
    if faqs:
        graph.append({
            "@type": "FAQPage",
            "mainEntity": [{
                "@type": "Question",
                "name": q,
                "acceptedAnswer": {"@type": "Answer", "text": a}
            } for q, a in faqs]
        })
    if len(trail) > 1:
        graph.append({
            "@type": "BreadcrumbList",
            "itemListElement": [{
                "@type": "ListItem",
                "position": i + 1,
                "name": n,
                "item": f"{DOMAIN}{u}"
            } for i, (n, u) in enumerate(trail)]
        })
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False) + '</script>'

def page(path,title,desc,h1,lead,body,trail,faqs=None):
    bc=" &rsaquo; ".join(f'<a href="{BASE}{u}">{n}</a>' if i<len(trail)-1 else n for i,(n,u) in enumerate(trail))
    crumb=f'<nav class="crumb w" aria-label="Breadcrumb">{bc}</nav>' if len(trail)>1 else ""
    ld=schema(trail, faqs)
    locs=" ".join(f'<a href="{BASE}{url(l["slug"])}">{l["name"]}</a>' for l in LOCS)
    return f'''<!doctype html><html lang="en-IN"><head>
<script async src="https://www.googletagmanager.com/gtm.js?id=GTM-53L3GBT7"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
</script>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc)}"><meta name="google-site-verification" content="AGyL0ygXGcdupr7cqQcWE9-Uh1IIci3rVoyYxQLJXzg"><link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:image" content="{DOMAIN}/assets/stretch-film-pallet-hero.webp"><meta property="og:type" content="website">
<link rel="icon" href="{BASE}/favicon.ico" sizes="48x48"><link rel="icon" type="image/png" href="{BASE}/assets/icon-192.png" sizes="192x192"><link rel="apple-touch-icon" href="{BASE}/assets/apple-touch-icon.png"><style>{CSS}</style>{ld}</head><body>
<header><div class="w bar"><a class="logo" href="{BASE}/"><img src="{BASE}/assets/logo.webp" width="40" height="40" alt="SAINI TRADERS logo"><span>SAINI <b>TRADERS</b></span></a><nav aria-label="Main"><a href="{BASE}{PARENT}">Stretch Film</a><a href="{BASE}{url("kanpur")}">Kanpur</a><a href="#contact">Contact</a></nav></div></header>
{crumb}
<section class="hero"><div class="w"><div><h1>{h1}</h1><p>{lead}</p><a class="btn" href="{WA_MSG}" rel="noopener">WhatsApp enquiry</a><a class="btn o" href="tel:+919140948445">Call 09140948445</a></div><div>{ROLL}</div></div></section>
<main class="w">{body}</main>
<section class="cta" id="contact"><div class="w"><h2>Contact {NAME}</h2><p>{ADDR}<br>Open Monday to Sunday, 9:00 AM to 8:00 PM</p><p>Phone: <a href="tel:+919140948445">09140948445</a> / <a href="tel:+917786843061">07786843061</a></p><a class="btn" href="{WA_MSG}" rel="noopener">Chat on WhatsApp</a> <a class="btn o" href="{DIR}" rel="noopener">Get directions</a> <a class="btn o" href="{GBP}" rel="noopener">View on Google Maps</a></div></section>
<div class="w" style="padding-top:24px"><iframe class="map" title="SAINI TRADERS location map, Ispat Nagar, Kanpur" loading="lazy" referrerpolicy="no-referrer-when-downgrade" src="{EMBED}"></iframe></div>
<footer><div class="w"><p><strong>{NAME}</strong>, packaging company, Kanpur.</p><p>{locs}</p></div></footer>
<a class="btn fab" href="{WA_MSG}" rel="noopener" aria-label="Chat on WhatsApp">WhatsApp</a></body></html>'''

def faq(items): return "".join(f"<details><summary>{q}</summary><p>{a}</p></details>" for q,a in items)

PRODUCTS = [("Hand grade stretch film","Rolls applied by hand or with a simple dispenser. Suited to parcels, furniture and low to moderate pallet volumes."),
("Machine grade stretch film","Rolls made for pallet wrapping machines, for consistent wrapping at higher volumes."),
("Transparent stretch film","Clear film that lets you see and scan contents, labels and barcodes without unwrapping."),
("Black stretch film","Opaque film for concealing contents or shielding them from light during storage and transit.")]
def products(): return '<div class="grid">'+"".join(f'<div class="card"><h3>{a}</h3><p>{b}</p></div>' for a,b in PRODUCTS)+"</div>"

def write(path,content):
    d=os.path.join(OUT,path.strip("/")); os.makedirs(d,exist_ok=True)
    open(os.path.join(d,"index.html"),"w",encoding="utf-8").write(content)

# parent
paras="".join(f'<div class="loc"><h3>Stretch Film Supplier in {l["name"]}</h3><p>{l["para"].format(link=f"<a href=\"{BASE}{url(l[chr(115)+chr(108)+chr(117)+chr(103)])}\">Stretch Film Supplier in {l[chr(110)+chr(97)+chr(109)+chr(101)]}</a>")}</p></div>' for l in LOCS)
pbody=f'''<h2>Industrial Stretch Film Rolls for Packaging</h2>
<div class="pic"><img src="{BASE}/assets/stretch-film-rolls.webp" width="480" height="638" loading="lazy" decoding="async" alt="Rows of transparent stretch film rolls with cardboard cores"></div><p>SAINI TRADERS is a packaging company at Ispat Nagar, Kanpur. We handle industrial stretch film rolls used to hold, stabilise and protect goods during storage and transit. Whether you wrap a few parcels a week or several pallets a day, you can enquire with us about the film that suits your work.</p>
<h2>Types of Stretch Film Available</h2>{products()}
<h3 style="margin-top:20px">Hand Grade Stretch Film</h3><p>A practical choice for small units, shops and sellers. It needs no machine and is easy to apply around cartons, furniture and mixed loads.</p>
<h3>Machine Grade Stretch Film</h3><p>Built for wrapping machines, where steady tension and speed matter. Often chosen by factories and warehouses with regular pallet output.</p>
<h3>Transparent Stretch Film</h3><p>The everyday choice when labels and contents should stay visible during handling and inventory checks.</p>
<h3>Black Stretch Film</h3><p>Used when contents should not be seen or when light exposure is a concern.</p>
<h2>Stretch Film Applications</h2><div class="grid"><div class="card"><h3>Pallet wrapping</h3><p>Binds cartons and sacks into one stable unit.</p></div><div class="card"><h3>Industrial packaging</h3><p>Bundles parts, pipes, rolls and machine components.</p></div><div class="card"><h3>Shipment protection</h3><p>Shields parcels from dust, scuffs and handling marks.</p></div><div class="card"><h3>Manufacturing</h3><p>Keeps finished goods together between line and dispatch.</p></div></div>
<h2>Stretch Film for Factories, Warehouses and Logistics</h2><p>Factories use stretch film at dispatch, warehouses use it to keep stored stock together, and logistics operators use it to protect consignments while they change hands. Each setting has its own volume and handling pattern, so tell us how you pack and we can discuss the right grade and roll size.</p>
<h2>Single Roll and Bulk Stretch Film Supply</h2><p>Single-roll enquiries are welcome from small businesses and individuals, and we also discuss bulk requirements. We do not list prices on this website because requirements differ; contact us and we will respond to your enquiry.</p>
<h2>Stretch Film Supplier Near You in Kanpur and Nearby Areas</h2><p>Our only address is D-95, Ispat Nagar, Kanpur. The pages below explain how we can help in each area. They are guides to local packaging needs, not separate branches.</p>{paras}
<h2>Frequently Asked Questions</h2>{faq(FAQ_PARENT)}'''
write(PARENT,page(PARENT,"Stretch Film Supplier Near Me in Kanpur | SAINI TRADERS","Hand-grade, machine-grade, transparent and black stretch film from SAINI TRADERS, Ispat Nagar, Kanpur. Call or WhatsApp for single-roll and bulk enquiries.","Stretch Film Supplier Near Me in Kanpur","Industrial stretch film rolls for pallet wrapping and packaging. Enquire by WhatsApp or phone.",pbody,[("Home","/"),("Stretch Film Supplier Near Me",PARENT)],FAQ_PARENT))

# children
for l in LOCS:
    nearl=" ".join(f'See also our <a href="{BASE}{url(n)}">stretch film supplier page for {BY[n]["name"]}</a>.' for n in l["near"])
    lead = l.get("custom_lead") or "Enquire about stretch film rolls from SAINI TRADERS, Ispat Nagar, Kanpur."
    if l["slug"] == "dada-nagar":
        body=f'''<p style="margin-top:24px"><strong>Saini Traders</strong> is a local <a href="{BASE}{PARENT}">stretch film supplier</a> serving the Dada Nagar industrial belt, minutes from <strong>Dada Nagar Chauraha</strong> and <strong>Coca Cola Chauraha</strong>. We supply hand-grade and machine-grade stretch film, BOPP tape and wrapping material straight from our own stock across <a href="{BASE}{url("kanpur")}">Kanpur</a>.</p>
<div class="trust-bar">⭐ 5-star rated by 6 local buyers on Google &nbsp;|&nbsp; 🚚 Same-day dispatch &nbsp;|&nbsp; ⚖️ Proper weight, exact micron</div>
<p>📞 <strong>Call:</strong> <a href="tel:+919140948445">09140948445</a> / <a href="tel:+917786843061">07786843061</a> &nbsp;|&nbsp; 💬 <strong>WhatsApp for today’s rate:</strong> <a href="{WA_MSG}" rel="noopener">Chat on WhatsApp</a></p>

<h2>Packing Material Ki Teen Sabse Badi Problems, Aur Hamara Solution</h2>
<p>Dada Nagar ke zyada tar buyers ye teen dikkatein jhelte hain:</p>
<ul class="clean">
  <li><strong>Short weight:</strong> roll ka weight kam, core bhaari</li>
  <li><strong>Wrong micron:</strong> patli film, pallet par phat jati hai</li>
  <li><strong>Late delivery:</strong> outstation dealer se maal aane tak line ruk jati hai</li>
</ul>
<div class="trust-bar"><strong>Hamara tareeka:</strong> net weight aur core weight declared, ordered micron hi supply, aur local stock se same-day dispatch.</div>

<h2>Local Supplier vs Outstation Dealer</h2>
<div class="tbl-wrap">
  <table class="cmp">
    <thead>
      <tr><th>Parameter</th><th>Saini Traders (Dada Nagar)</th><th>Outstation Dealer</th></tr>
    </thead>
    <tbody>
      <tr><td><strong>Delivery</strong></td><td>Same day, within hours</td><td>2–5 days</td></tr>
      <tr><td><strong>Freight</strong></td><td>Minimal</td><td>Extra, transporter charges</td></tr>
      <tr><td><strong>Weight check</strong></td><td>At delivery, in front of you</td><td>Dispute mushkil</td></tr>
      <tr><td><strong>Urgent order</strong></td><td>Call karo, maal nikla</td><td>Wait karna padta hai</td></tr>
      <tr><td><strong>Support</strong></td><td>Seedha shop se baat</td><td>Agent ke through</td></tr>
    </tbody>
  </table>
</div>

<h2>Why Factories in Dada Nagar Trust Saini Traders</h2>
<div class="grid">
  <div class="card"><h3>Direct rate, no middlemen</h3><p>Hum local stock se hi dispatch karte hain. Outstation freight aur dealer chain ka extra markup aapke rate mein nahi judta.</p></div>
  <div class="card"><h3>Zero weight-fudge</h3><p>Har roll tola jata hai. Aap ya aapka store keeper delivery par khud weigh kar sakte ho.</p></div>
  <div class="card"><h3>Exact micron, every batch</h3><p>Jo micron order karoge wahi milega. Pallet par film tight rahegi, wastage kam hoga.</p></div>
  <div class="card"><h3>Credit and regular supply</h3><p>Weekly ya monthly order karte ho? Regular credit terms aur monthly supply ke baare mein poochho. Regular buyers ke liye stock ready rehta hai.</p></div>
</div>

<h2>Fast Dispatch Near Dada Nagar Chauraha and Coca Cola Chauraha</h2>
<p>Hamari location hi hamara advantage hai:</p>
<ul class="clean">
  <li><strong>Dada Nagar Chauraha:</strong> main crossing ke factories ko sabse tez delivery</li>
  <li><strong>Coca Cola Chauraha:</strong> crossing ke units aur peeche ki lanes</li>
  <li><strong>SBI Bank branch near the Police Station:</strong> pickup ya visit ke liye aasan landmark</li>
  <li><strong>Main Dada Nagar industrial belt aur factory lanes:</strong> gate, godown ya dispatch section tak delivery</li>
</ul>
<p><strong>Typical delivery:</strong> 2–4 hours within Dada Nagar. Orders confirmed before 5:00 PM usi din dispatch hote hain.</p>
<p>Lane ka confirm nahi? WhatsApp par location bhejo, hum timing bata denge.</p>
<p>📞 <a href="tel:+919140948445">09140948445</a> / <a href="tel:+917786843061">07786843061</a> &nbsp;|&nbsp; 💬 <a href="{WA_MSG}" rel="noopener">WhatsApp for today’s rate</a></p>

<h2>Hamare Products</h2>
<figure class="feat-img">
  <img src="{BASE}/assets/stretch-film-sizes-dada-nagar.jpg" width="720" height="540" loading="lazy" decoding="async" alt="Stretch film rolls in all sizes from small hand rolls to jumbo and machine grade rolls at Saini Traders Dada Nagar Kanpur">
  <figcaption>All stretch film roll sizes ready in stock — from compact hand rolls to heavy-duty machine-grade and jumbo rolls.</figcaption>
</figure>
{products()}
<p style="margin-top:14px">Explore our complete <a href="{BASE}{PARENT}">stretch film product range and specifications</a> (hand-grade, machine-grade, jumbo rolls, and BOPP tape).</p>

<h2>Hand-Grade ya Machine-Grade: Kaunsa Lein?</h2>
<ul class="clean">
  <li><strong>Hand-grade:</strong> agar roz kam pallets wrap karte ho aur kaam manual hai</li>
  <li><strong>Machine-grade:</strong> agar wrapping machine hai ya dispatch volume zyada hai, isme film kam lagti hai</li>
  <li><strong>Jumbo roll:</strong> agar bahut zyada pallets hain aur roll change ka downtime kam karna hai</li>
</ul>
<p>Pakka nahi pata? Apna product aur daily volume batao, hum sahi grade suggest karenge.</p>

<h2>Industries We Supply</h2>
<div class="grid">
  <div class="card"><h3>Leather aur footwear</h3><p>Bundles aur cartons ka pallet stability.</p></div>
  <div class="card"><h3>Packaging aur printing</h3><p>Finished goods ki dust-free wrapping.</p></div>
  <div class="card"><h3>FMCG aur food products</h3><p>Carton pallets ka safe dispatch.</p></div>
  <div class="card"><h3>Chemical, plastic, steel</h3><p>Heavy loads ki secure binding.</p></div>
  <div class="card"><h3>Textile aur garment</h3><p>Bales aur boxes ki wrapping.</p></div>
  <div class="card"><h3>Transporters aur warehouses</h3><p>Loading se pehle load locking.</p></div>
</div>

<h2>What Our Buyers Say</h2>
<div class="grid">
  <div class="card"><h3>⭐⭐⭐⭐⭐ Verified Factory Buyer</h3><p>“Proper roll weight aur exact micron milta hai. Dada Nagar factory mein same-day maal aa jata hai.”</p></div>
  <div class="card"><h3>⭐⭐⭐⭐⭐ Industrial Unit, Dada Nagar</h3><p>“Direct wholesale rate hai aur core weight pehle se clear rehta hai. Urgent dispatch ke liye best supplier.”</p></div>
  <div class="card"><h3>⭐⭐⭐⭐⭐ Packaging &amp; Dispatch Buyer</h3><p>“Hand-grade aur machine-grade dono rolls ki quality consistent hai. Ek call par turant delivery milti hai.”</p></div>
</div>
<p style="margin-top:14px">👉 <a href="{GBP}" rel="noopener">Google par saare reviews dekho (Google Business Profile)</a></p>

<h2>Urgent Requirement? Order Aise Hota Hai</h2>
<ol class="clean">
  <li><strong>Call ya WhatsApp karo:</strong> micron, roll weight, quantity batao.</li>
  <li><strong>Rate aur timing:</strong> kuch minutes mein confirm.</li>
  <li><strong>Order confirm:</strong> hum seedha local stock se dispatch karte hain.</li>
  <li><strong>Gate delivery:</strong> delivery factory gate par, weight check ke saath.</li>
</ol>

<h2>About Saini Traders</h2>
<p><strong>Saini Traders</strong> Dada Nagar aur Ispat Nagar, Kanpur ka trusted industrial packaging supplier hai. Hum local factories ko <a href="{BASE}{PARENT}">stretch film rolls</a>, BOPP tape aur wrapping material direct wholesale rate par supply kar rahe hain. {nearl} Also serving <a href="{BASE}{url("kidwai-nagar")}">Kidwai Nagar</a>, <a href="{BASE}{url("shastri-nagar")}">Shastri Nagar</a>, and <a href="{BASE}{url("unnao")}">Unnao</a>.</p>

<h2>Frequently Asked Questions</h2>{faq(l["faqs"])}

<h2>Get Today’s Stretch Film Rate in Dada Nagar</h2>
<p>Micron, weight aur quantity bhejo, hum rate aur delivery time ke saath turant reply karenge.</p>
<p>📞 <strong>Phone:</strong> <a href="tel:+919140948445">09140948445</a> / <a href="tel:+917786843061">07786843061</a> &nbsp;|&nbsp; 💬 <strong>WhatsApp:</strong> <a href="{WA_MSG}" rel="noopener">Click here for today’s rate</a></p>'''
    else:
        body=f'''<h2>About stretch film supply for {l["name"]}</h2><p>{l["intro"]}</p>
<h2>{l["h2"]}</h2><p>{l["focus"]}</p><p>{l["tip"]}</p>
<h2>Stretch film we handle</h2>{products()}
<p style="margin-top:16px"><a href="{BASE}{PARENT}">Explore our complete stretch film product range.</a> {nearl}</p>
<h2>Where to find us</h2><p>Our address is {ADDR}. This is our only location; {l["name"]} customers reach us by phone, WhatsApp or a visit during business hours.</p>
<h2>Frequently Asked Questions</h2>{faq(l["faqs"])}'''
    write(url(l["slug"]),page(url(l["slug"]),l["title"],l["desc"],l["h1"],lead,body,[("Home","/"),("Stretch Film Supplier Near Me",PARENT),(l["h1"],url(l["slug"]))],l["faqs"]))

# home
hbody=f'''<h2>Packaging company in Kanpur</h2><p>SAINI TRADERS supplies stretch film rolls for factories, warehouses, traders and small businesses in and around Kanpur.</p>
<p><a class="btn" href="{BASE}{PARENT}" style="color:#0b2447">View stretch film range</a></p>
<h2>Areas we receive enquiries from</h2><div class="grid">{"".join(f'<div class="card"><h3><a href="{BASE}{url(l["slug"])}">{l["name"]}</a></h3></div>' for l in LOCS)}</div>
<h2>Frequently Asked Questions</h2>{faq(FAQ_PARENT)}'''
write("/",page("/","SAINI TRADERS | Packaging Company in Kanpur","SAINI TRADERS, Ispat Nagar, Kanpur: stretch film rolls for industrial packaging. Call or WhatsApp for enquiries.","SAINI TRADERS, Packaging Company in Kanpur","Stretch film for pallet wrapping and industrial packaging.",hbody,[("Home","/")],FAQ_PARENT))

urls=["/",PARENT]+[url(l["slug"]) for l in LOCS]
open(OUT+"/sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u in urls)+"</urlset>")
robots_content = f"""User-agent: *
Allow: /
Disallow:

# Explicitly Allow All Major AI & Search Crawlers (AEO / GEO Ready)
User-agent: GPTBot
Allow: /

User-agent: OAI-SearchBot
Allow: /

User-agent: ChatGPT-User
Allow: /

User-agent: Googlebot
Allow: /

User-agent: Google-Extended
Allow: /

User-agent: ClaudeBot
Allow: /

User-agent: Claude-Web
Allow: /

User-agent: anthropic-ai
Allow: /

User-agent: PerplexityBot
Allow: /

User-agent: Bingbot
Allow: /

User-agent: Applebot-Extended
Allow: /

User-agent: meta-externalagent
Allow: /

User-agent: CCBot
Allow: /

Sitemap: {DOMAIN}/sitemap.xml
"""
open(OUT+"/robots.txt","w").write(robots_content)
open(OUT+"/CNAME","w").write("packagingtraders.in\n")


