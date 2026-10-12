#!/usr/bin/env python3
"""Static site generator for Alkarar Arrow (Arabic + English).

Run `python3 build.py` after editing the content below. It rewrites every
HTML page, sitemap.xml and 404.html. No dependencies beyond Python 3.
"""
import json, os

SITE = "https://alkarararrow.com"
EMAIL = "info@alkarararrow.com"
PHONE_DISPLAY = "00966504779551"
PHONE_TEL = "+966504779551"
CR = "7050745707"
ROOT = os.path.dirname(os.path.abspath(__file__))

ICONS = {
 "food": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><path d="M24 42V14"/><path d="M24 14c-6 0-9-4-9-9 6 0 9 4 9 9z"/><path d="M24 14c6 0 9-4 9-9-6 0-9 4-9 9z"/><path d="M24 26c-6 0-9-4-9-9 6 0 9 4 9 9z"/><path d="M24 26c6 0 9-4 9-9-6 0-9 4-9 9z"/><path d="M24 38c-6 0-9-4-9-9 6 0 9 4 9 9z"/><path d="M24 38c6 0 9-4 9-9-6 0-9 4-9 9z"/></svg>',
 "technology": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><rect x="12" y="12" width="24" height="24"/><rect x="19" y="19" width="10" height="10"/><path d="M18 12V5M24 12V5M30 12V5M18 43v-7M24 43v-7M30 43v-7M12 18H5M12 24H5M12 30H5M43 18h-7M43 24h-7M43 30h-7"/></svg>',
 "contracting": '<svg class="icon" viewBox="0 0 48 48" aria-hidden="true"><path d="M6 42h36"/><path d="M10 42V20l14-10 14 10v22"/><path d="M19 42V28h10v14"/><path d="M24 10V4"/></svg>',
}

# ----------------------------------------------------------------- content
T = {
"ar": {
 "dir": "rtl", "lang": "ar", "base": "/", "other": "en", "other_label": "English", "other_short": "EN",
 "fonts": "https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@500;600;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500&display=swap",
 "brand": "سهم الكرار", "locale": "ar_SA", "other_locale": "en_US",
 "skip": "انتقل إلى المحتوى",
 "nav": {"about": "عن الشركة", "divisions": "قطاعاتنا", "contact": "تواصل معنا"},
 "home_label": "الرئيسية",
 "div_names": {"food": "الأغذية", "technology": "التقنية", "contracting": "المقاولات"},
 "home": {
  "title": "سهم الكرار | الأغذية والتقنية والمقاولات في المملكة العربية السعودية",
  "desc": "سهم الكرار مجموعة سعودية في الرياض تعمل في الأغذية والتقنية والمقاولات. نبدأ بثبات، ونُنفّذ بدقة، ونلتزم بما نعد به.",
  "eyebrow": "الرياض · المملكة العربية السعودية",
  "h1": "إقدامٌ يُصيب الهدف",
  "lead": "مجموعة سعودية تعمل في الأغذية والتقنية والمقاولات. نبدأ بثبات، ونُنفّذ بدقة، ونلتزم بما نعد به.",
  "cta1": "تواصل معنا", "cta2": "قطاعاتنا",
  "logo_alt": "شعار سهم الكرار",
  "about_eyebrow": "عن الشركة",
  "about_h": "اسمٌ يحمل معنى الإقدام",
  "about_p": "الكرّار هو من يكرّ على الهدف ولا يتراجع، والسهم هو الدقة في الإصابة. من هذين المعنيين جاء اسم الشركة وشعارها: صقر وسهم ودرع، ثلاث صور لثبات الاتجاه وقوة الحماية وسرعة التنفيذ.",
  "principles": [("الثبات", "نختار اتجاهنا بعناية، ثم نمضي فيه حتى النتيجة."),
                 ("الدقة", "جودة محسوبة في كل مرحلة، من التوريد إلى التسليم."),
                 ("الالتزام", "مواعيد واضحة ووعود قابلة للقياس مع كل عميل وشريك.")],
  "div_eyebrow": "قطاعاتنا", "div_h": "ثلاثة قطاعات، هوية واحدة", "more": "تعرّف على القطاع",
  "contact_eyebrow": "تواصل معنا", "contact_h": "لديك مشروع أو توريد؟ نبدأ من هنا",
  "contact_p": "اكتب لنا عن احتياجك، وسيعود إليك فريق القطاع المختص.",
 },
 "labels": {"email": "البريد الإلكتروني", "phone": "الهاتف", "hq": "المقر الرئيسي", "cr": "السجل التجاري",
            "hq_val": "الرياض، غرناطة، طريق الإمام عبدالله بن سعود",
            "parent": "الشركة الأم: الإسكندرية، فرجينيا، الولايات المتحدة الأمريكية",
            "contact_h": "تواصل", "div_h": "القطاعات", "company_h": "الشركة", "privacy": "سياسة الخصوصية",
            "rights": "جميع الحقوق محفوظة"},
 "divs": {
  "food": {
   "title": "الأغذية | سهم الكرار",
   "desc": "قطاع الأغذية في سهم الكرار: توريد وتجارة اللحوم والسكر والمواد الغذائية الأساسية للقطاعين الحكومي والخاص في المملكة العربية السعودية.",
   "short": "توريد وتجارة المنتجات الغذائية بجودة موثوقة وسلاسل إمداد منضبطة.",
   "bullets": ["اللحوم والمنتجات الغذائية", "السكر والمواد الأساسية", "التوريد للقطاعين الحكومي والخاص"],
   "h1": "الأغذية",
   "lead": "نورّد ونتاجر في المنتجات الغذائية الأساسية لعملاء القطاعين الحكومي والخاص، بجودة موثوقة وسلاسل إمداد منضبطة.",
   "services_h": "ما نقدمه",
   "services": [("اللحوم", "لحوم الضأن والماعز والأبقار والدواجن للمطاعم والمنشآت والجهات."),
                ("السكر والمواد الأساسية", "توريد السكر والسلع الغذائية الأساسية بكميات تناسب احتياج العميل."),
                ("التوريد للجهات", "عقود توريد منتظمة للجهات الحكومية والشركات، بمواعيد واضحة."),
                ("الجودة والامتثال", "نعمل وفق اشتراطات الجهات الرقابية في المملكة ونوثّق مراحل التوريد.")],
   "cta_h": "تحتاج توريد أغذية لجهتك؟", "cta_p": "أرسل لنا الأصناف والكميات والموعد، ونعود إليك بعرض.", "cta_btn": "اطلب عرض سعر",
   "subject": "طلب عرض سعر - قطاع الأغذية"},
  "technology": {
   "title": "التقنية | سهم الكرار",
   "desc": "قطاع التقنية في سهم الكرار: الذكاء الاصطناعي وأتمتة الأعمال، تقنية المعلومات والشبكات، الأمن السيبراني، والاستشارات التقنية، مع نظام إدارة الاستقدام كمشروع سابق.",
   "short": "حلول الذكاء الاصطناعي وتقنية المعلومات والشبكات، مع استشارات تقنية للجهات والشركات.",
   "bullets": ["الذكاء الاصطناعي وأتمتة الأعمال", "تقنية المعلومات والشبكات", "الاستشارات التقنية"],
   "h1": "التقنية",
   "lead": "نبني حلولًا تقنية تخدم العمل مباشرة: ذكاء اصطناعي وأتمتة، وبنية تقنية وشبكات، وأنظمة مخصصة تُصمَّم حول طريقة عمل العميل.",
   "services_h": "ما نقدمه",
   "services": [("الذكاء الاصطناعي وأتمتة الأعمال", "أتمتة الإجراءات المتكررة وبناء حلول ذكية تختصر الوقت وتقلل الأخطاء."),
                ("تقنية المعلومات والشبكات", "تصميم الشبكات وتشغيلها ودعمها بما يناسب حجم المنشأة."),
                ("الأمن السيبراني", "فحص الاختراق وتقييم الثغرات وخدمات المراقبة والتشغيل الأمني."),
                ("الأنظمة المخصصة", "تطوير أنظمة من الصفر حسب إجراءات العميل، بدل تطويع العميل لنظام جاهز."),
                ("الاستشارات التقنية", "تقييم الوضع الحالي وتحديد الأولويات وخارطة طريق واضحة للتنفيذ.")],
   "work_eyebrow": "من أعمالنا السابقة", "work_h": "مثال: نظام إدارة الاستقدام",
   "work_tag": "مشروع سابق", "work_name": "نظام إدارة الاستقدام",
   "work_p": "نظام متكامل لإدارة عمليات الاستقدام، بُني من الصفر ليناسب طبيعة عمل شركات الاستقدام، ونُفّذ لإحدى الشركات العاملة في هذا المجال.",
   "work_feats": [("مصمم حسب الطلب", "يُبنى على إجراءات الشركة، لا العكس."),
                  ("على خوادم العميل", "يمكن نشره داخل بيئة الشركة لتبقى بياناتها عندها."),
                  ("هوية العميل", "يقبل شعار الشركة وألوانها ليظهر باسمها.")],
   "cta_h": "عندك فكرة أو نظام تحتاج بناءه؟", "cta_p": "أخبرنا عن الإجراء الذي تريد تبسيطه، ونقترح عليك الحل.", "cta_btn": "ناقش مشروعك",
   "subject": "استفسار - قطاع التقنية"},
  "contracting": {
   "title": "المقاولات | سهم الكرار",
   "desc": "قطاع المقاولات في سهم الكرار: مقاولات عامة وإدارة وتنفيذ المشاريع والصيانة والتشغيل بمعايير جودة وسلامة والتزام بالجداول الزمنية في المملكة العربية السعودية.",
   "short": "تنفيذ وإدارة المشاريع بمعايير جودة وسلامة والتزام بالجداول الزمنية.",
   "bullets": ["المقاولات العامة", "إدارة وتنفيذ المشاريع", "الصيانة والتشغيل"],
   "h1": "المقاولات",
   "lead": "ننفّذ ونُدير المشاريع بمعايير جودة وسلامة واضحة، وبجدول زمني يعرفه العميل من اليوم الأول.",
   "services_h": "ما نقدمه",
   "services": [("المقاولات العامة", "تنفيذ أعمال المقاولات للمنشآت والمشاريع الحكومية والخاصة."),
                ("إدارة المشاريع", "تخطيط ومتابعة التنفيذ والتكلفة والجودة حتى التسليم."),
                ("الصيانة والتشغيل", "عقود صيانة وتشغيل تحافظ على المنشأة جاهزة للعمل."),
                ("السلامة والجودة", "التزام بإجراءات السلامة والجودة في كل موقع.")],
   "cta_h": "لديك مشروع للتنفيذ؟", "cta_p": "أرسل لنا نطاق العمل والموقع والموعد المطلوب، ونعود إليك بعرض.", "cta_btn": "اطلب عرض سعر",
   "subject": "طلب عرض سعر - قطاع المقاولات"},
 },
 "privacy": {
  "title": "سياسة الخصوصية | سهم الكرار",
  "desc": "كيف تتعامل سهم الكرار مع البيانات التي تصلها عبر البريد الإلكتروني وموقعها.",
  "h1": "سياسة الخصوصية",
  "body": [
   ("البيانات التي نجمعها", "لا يجمع هذا الموقع بيانات من الزوار تلقائيًا. إذا راسلتنا عبر البريد الإلكتروني أو الهاتف، فإننا نستلم الاسم وبيانات التواصل وما تكتبه لنا."),
   ("كيف نستخدمها", "نستخدم هذه البيانات للرد على طلبك وتقديم العرض أو الخدمة المطلوبة، ولا نبيعها ولا نشاركها لأغراض تسويقية."),
   ("مدة الاحتفاظ", "نحتفظ بالمراسلات المدة اللازمة لخدمتك والالتزام بالأنظمة المعمول بها، ثم نحذفها."),
   ("حقوقك", "يحق لك طلب الاطلاع على بياناتك أو تصحيحها أو حذفها وفق نظام حماية البيانات الشخصية في المملكة."),
   ("للتواصل", "لأي استفسار عن الخصوصية راسلنا على " + EMAIL + "."),
  ]},
},
"en": {
 "dir": "ltr", "lang": "en", "base": "/en/", "other": "ar", "other_label": "العربية", "other_short": "عربي",
 "fonts": "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500&display=swap",
 "brand": "Alkarar Arrow", "locale": "en_US", "other_locale": "ar_SA",
 "skip": "Skip to content",
 "nav": {"about": "About", "divisions": "Divisions", "contact": "Contact"},
 "home_label": "Home",
 "div_names": {"food": "Food", "technology": "Technology", "contracting": "Contracting"},
 "home": {
  "title": "Alkarar Arrow | Food, Technology and Contracting in Saudi Arabia",
  "desc": "Alkarar Arrow is a Saudi group based in Riyadh working in food, technology and contracting. We start with conviction, deliver with precision, and keep what we promise.",
  "eyebrow": "Riyadh · Saudi Arabia",
  "h1": "Boldness that hits the mark.",
  "lead": "A Saudi group working in food, technology and contracting. We start with conviction, deliver with precision, and keep what we promise.",
  "cta1": "Contact us", "cta2": "Our divisions",
  "logo_alt": "Alkarar Arrow logo",
  "about_eyebrow": "About",
  "about_h": "A name that carries the meaning of courage",
  "about_p": "Al-Karrar is the one who charges the objective and does not turn back; the arrow is precision in hitting it. From those two ideas came the name and the mark: a falcon, an arrow and a shield, standing for steady direction, strong protection and fast execution.",
  "principles": [("Conviction", "We choose our direction carefully, then hold it until the result."),
                 ("Precision", "Measured quality at every stage, from sourcing to handover."),
                 ("Commitment", "Clear dates and measurable promises for every client and partner.")],
  "div_eyebrow": "Divisions", "div_h": "Three divisions, one identity", "more": "Explore the division",
  "contact_eyebrow": "Contact", "contact_h": "A project or a supply need? Start here.",
  "contact_p": "Tell us what you need, and the team for the right division will get back to you.",
 },
 "labels": {"email": "Email", "phone": "Phone", "hq": "Headquarters", "cr": "C.R. number",
            "hq_val": "Riyadh, Granada, Imam Abdullah bin Saud Road",
            "parent": "Parent company: Alexandria, Virginia, United States of America",
            "contact_h": "Contact", "div_h": "Divisions", "company_h": "Company", "privacy": "Privacy policy",
            "rights": "All rights reserved"},
 "divs": {
  "food": {
   "title": "Food | Alkarar Arrow",
   "desc": "Alkarar Arrow's food division: sourcing and trading of meat, sugar and staple food products for government and private clients in Saudi Arabia.",
   "short": "Sourcing and trading of food products with reliable quality and disciplined supply chains.",
   "bullets": ["Meat and food products", "Sugar and staple goods", "Supply to government and private sectors"],
   "h1": "Food",
   "lead": "We source and trade staple food products for government and private clients, with reliable quality and a disciplined supply chain.",
   "services_h": "What we offer",
   "services": [("Meat", "Lamb, goat, beef and poultry for restaurants, facilities and institutions."),
                ("Sugar and staples", "Supply of sugar and basic food goods in quantities that fit the client's need."),
                ("Supply to institutions", "Regular supply contracts for government bodies and companies, with clear delivery dates."),
                ("Quality and compliance", "We work to the requirements of the Kingdom's regulators and document each stage of supply.")],
   "cta_h": "Need food supply for your organisation?", "cta_p": "Send us the items, quantities and date, and we will come back with a quotation.", "cta_btn": "Request a quotation",
   "subject": "Quotation request - Food division"},
  "technology": {
   "title": "Technology | Alkarar Arrow",
   "desc": "Alkarar Arrow's technology division: AI and business automation, IT and networking, cybersecurity and technology consulting, with a recruitment management system as previous work.",
   "short": "AI, IT and networking solutions, with technology consulting for organisations and companies.",
   "bullets": ["AI and business automation", "IT and networking", "Technology consulting"],
   "h1": "Technology",
   "lead": "We build technology that serves the work directly: AI and automation, infrastructure and networks, and custom systems designed around how the client operates.",
   "services_h": "What we offer",
   "services": [("AI and business automation", "Automating repetitive processes and building smart tools that save time and reduce errors."),
                ("IT and networking", "Network design, operation and support sized to the organisation."),
                ("Cybersecurity", "Penetration testing, vulnerability assessment and security monitoring and operations."),
                ("Custom systems", "Systems built from scratch around the client's procedures, instead of bending the client to an off-the-shelf product."),
                ("Technology consulting", "Assessing the current state, setting priorities and a clear roadmap to execute.")],
   "work_eyebrow": "Previous work", "work_h": "Example: a recruitment management system",
   "work_tag": "Previous work", "work_name": "Recruitment management system",
   "work_p": "An end-to-end system for managing recruitment (istiqdam) operations, built from scratch around how recruitment companies work, and delivered for a company in the field.",
   "work_feats": [("Built to order", "Shaped around the company's procedures, not the other way round."),
                  ("On the client's servers", "Can be deployed inside the company's own environment so its data stays with it."),
                  ("Client branding", "Takes the company's logo and colours so it appears under its own name.")],
   "cta_h": "Have an idea or a system you need built?", "cta_p": "Tell us which process you want to simplify and we will propose the solution.", "cta_btn": "Discuss your project",
   "subject": "Enquiry - Technology division"},
  "contracting": {
   "title": "Contracting | Alkarar Arrow",
   "desc": "Alkarar Arrow's contracting division: general contracting, project management and execution, and maintenance and operations to clear quality and safety standards in Saudi Arabia.",
   "short": "Delivery and management of projects to quality and safety standards, on schedule.",
   "bullets": ["General contracting", "Project management and execution", "Maintenance and operations"],
   "h1": "Contracting",
   "lead": "We deliver and manage projects to clear quality and safety standards, on a schedule the client knows from day one.",
   "services_h": "What we offer",
   "services": [("General contracting", "Construction works for facilities and for government and private projects."),
                ("Project management", "Planning and tracking execution, cost and quality through to handover."),
                ("Maintenance and operations", "Maintenance and operating contracts that keep a facility ready for use."),
                ("Safety and quality", "Safety and quality procedures followed on every site.")],
   "cta_h": "Have a project to deliver?", "cta_p": "Send us the scope, location and required date, and we will come back with a quotation.", "cta_btn": "Request a quotation",
   "subject": "Quotation request - Contracting division"},
 },
 "privacy": {
  "title": "Privacy policy | Alkarar Arrow",
  "desc": "How Alkarar Arrow handles the data it receives by email and through this website.",
  "h1": "Privacy policy",
  "body": [
   ("What we collect", "This website does not automatically collect data from visitors. If you contact us by email or phone, we receive your name, contact details and whatever you tell us."),
   ("How we use it", "We use it to answer your request and provide the quotation or service you asked for. We do not sell it or share it for marketing."),
   ("How long we keep it", "We keep correspondence for as long as needed to serve you and meet applicable regulations, then delete it."),
   ("Your rights", "You may ask to see, correct or delete your data under the Kingdom's Personal Data Protection Law."),
   ("Contact", "For any privacy question, write to " + EMAIL + "."),
  ]},
},
}
DIVS = ["food", "technology", "contracting"]

# ----------------------------------------------------------------- helpers
def esc(s): return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")

def path_for(lang, key):
    base = T[lang]["base"]
    return base if key == "home" else f"{base}{key}/"

def url(lang, key): return SITE + path_for(lang, key)

def head(lang, key, title, desc, extra_ld=None):
    t = T[lang]; o = t["other"]
    ld = ""
    for obj in (extra_ld or []):
        ld += f'<script type="application/ld+json">{json.dumps(obj, ensure_ascii=False)}</script>\n'
    return f'''<!doctype html>
<html lang="{t["lang"]}" dir="{t["dir"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url(lang, key)}">
<link rel="alternate" hreflang="{lang}" href="{url(lang, key)}">
<link rel="alternate" hreflang="{o}" href="{url(o, key)}">
<link rel="alternate" hreflang="x-default" href="{url('ar', key)}">
<meta name="theme-color" content="#0b0b0d">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{esc(t["brand"])}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{url(lang, key)}">
<meta property="og:image" content="{SITE}/assets/img/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="{t["locale"]}">
<meta property="og:locale:alternate" content="{t["other_locale"]}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}">
<meta name="twitter:image" content="{SITE}/assets/img/og-image.png">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/favicon-32.png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="manifest" href="/site.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{t["fonts"]}">
<link rel="stylesheet" href="/assets/css/style.css">
<script>document.documentElement.classList.add("js")</script>
{ld}</head>
'''

def header(lang, key):
    t = T[lang]; b = t["base"]; o = t["other"]
    logo = f'<img src="/assets/img/mark.png" alt="" width="46" height="48">'
    cur = lambda k: ' aria-current="page"' if key == k else ""
    div_links = "".join(f'<a href="{path_for(lang, d)}"{cur(d)}>{t["div_names"][d]}</a>' for d in DIVS)
    return f'''<a class="skip" href="#main">{t["skip"]}</a>
<header class="site">
  <a class="brand" href="{b}" aria-label="{esc(t["brand"])} - {t["home_label"]}">{logo}<span class="brand-name">{esc(t["brand"])}</span></a>
  <nav class="main" aria-label="{'التنقل الرئيسي' if lang == 'ar' else 'Main'}">
    <a href="{b}#about">{t["nav"]["about"]}</a>
    {div_links}
    <a href="{b}#contact">{t["nav"]["contact"]}</a>
    <a class="lang" href="{path_for(t["other"], key)}" hreflang="{o}" lang="{o}">{t["other_label"]}</a>
  </nav>
</header>
'''

def footer(lang):
    t = T[lang]; L = t["labels"]; b = t["base"]
    divs = "".join(f'<li><a href="{path_for(lang, d)}">{t["div_names"][d]}</a></li>' for d in DIVS)
    return f'''<footer class="site">
  <div class="wrap">
    <div class="stack g12"><a class="brand" href="{b}"><img src="/assets/img/mark.png" alt="" width="34" height="36" loading="lazy"><span class="brand-name" style="font-size:20px">{esc(t["brand"])}</span></a>
      <p>{L["parent"]}</p></div>
    <div><h2>{L["div_h"]}</h2><ul>{divs}</ul></div>
    <div><h2>{L["contact_h"]}</h2><ul>
      <li><a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a></li>
      <li><a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a></li>
      <li>{L["hq_val"]}</li></ul></div>
    <div><h2>{L["company_h"]}</h2><ul>
      <li>{L["cr"]}: <bdi>{CR}</bdi></li>
      <li><a href="{path_for(lang, "privacy")}">{L["privacy"]}</a></li></ul></div>
    <p class="fine">© 2026 {esc(t["brand"])}. {L["rights"]}.</p>
  </div>
</footer>
'''

def contact_rows(lang):
    L = T[lang]["labels"]
    return f'''<dl class="rows">
  <div><dt>{L["email"]}</dt><dd><a href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a></dd></div>
  <div><dt>{L["phone"]}</dt><dd><a href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a></dd></div>
  <div><dt>{L["hq"]}</dt><dd>{L["hq_val"]}</dd></div>
  <div><dt>{L["cr"]}</dt><dd><bdi>{CR}</bdi></dd></div>
</dl>'''

def org_ld(lang):
    t = T[lang]
    return {"@context": "https://schema.org", "@type": "Organization", "name": "Alkarar Arrow", "alternateName": "سهم الكرار",
            "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "email": EMAIL, "telephone": PHONE_TEL,
            "address": {"@type": "PostalAddress", "streetAddress": "Granada, Imam Abdullah bin Saud Road", "addressLocality": "Riyadh", "addressCountry": "SA"},
            "areaServed": "SA", "identifier": CR}

def crumb_ld(lang, key):
    t = T[lang]
    items = [(t["home_label"], url(lang, "home"))]
    if key != "home": items.append((t["div_names"].get(key, t["labels"]["privacy"]), url(lang, key)))
    return {"@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": n, "item": u} for i, (n, u) in enumerate(items)]}

def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(content)

# ----------------------------------------------------------------- pages
def home(lang):
    t = T[lang]; h = t["home"]; b = t["base"]
    cards = ""
    for d in DIVS:
        dv = t["divs"][d]
        lis = "".join(f"<li>{esc(x)}</li>" for x in dv["bullets"])
        cards += f'''<a class="card link" href="{path_for(lang, d)}">{ICONS[d]}<h3>{t["div_names"][d]}</h3><p>{esc(dv["short"])}</p><ul>{lis}</ul><span class="more">{h["more"]} {'←' if lang == 'ar' else '→'}</span></a>
'''
    princ = "".join(f'<div class="principle"><h3>{a}</h3><p>{c}</p></div>' for a, c in h["principles"])
    logo = "/assets/img/logo-ar.png" if lang == "ar" else "/assets/img/logo-en.png"
    body = f'''<body>
{header(lang, "home")}<main id="main">
<section class="hero">
  <div class="wrap cols" style="align-items:center">
    <div class="stack g28">
      <p class="eyebrow">{h["eyebrow"]}</p>
      <h1>{h["h1"]}</h1>
      <p class="lead">{h["lead"]}</p>
      <div class="btns"><a class="btn gold" href="#contact">{h["cta1"]}</a><a class="btn" href="#divisions">{h["cta2"]}</a></div>
    </div>
    <div class="hero-art"><img src="{logo}" alt="{h["logo_alt"]}" width="440" height="{ '486' if lang == 'ar' else '349'}" fetchpriority="high"></div>
  </div>
</section>
<section id="about" class="alt">
  <div class="wrap cols">
    <div class="stack g20"><p class="eyebrow">{h["about_eyebrow"]}</p><h2>{h["about_h"]}</h2><p class="muted">{h["about_p"]}</p></div>
    <div>{princ}</div>
  </div>
</section>
<section id="divisions">
  <div class="wrap stack g48">
    <div class="stack g12" style="max-width:640px"><p class="eyebrow">{h["div_eyebrow"]}</p><h2>{h["div_h"]}</h2></div>
    <div class="cards">{cards}</div>
  </div>
</section>
<section id="contact" class="alt">
  <div class="wrap cols">
    <div class="stack g20"><p class="eyebrow">{h["contact_eyebrow"]}</p><h2>{h["contact_h"]}</h2><p class="muted">{h["contact_p"]}</p></div>
    {contact_rows(lang)}
  </div>
</section>
</main>
{footer(lang)}<script src="/assets/js/main.js" defer></script>
</body></html>
'''
    return head(lang, "home", h["title"], h["desc"], [org_ld(lang)]) + body

def division(lang, d):
    t = T[lang]; dv = t["divs"][d]; b = t["base"]
    cards = "".join(f'<div class="card"><h3 style="font-size:24px">{esc(a)}</h3><p style="margin-top:10px">{esc(c)}</p></div>' for a, c in dv["services"])
    work = ""
    if d == "technology":
        feats = "".join(f"<div><strong>{esc(a)}</strong><span>{esc(c)}</span></div>" for a, c in dv["work_feats"])
        work = f'''<section class="alt" id="work">
  <div class="wrap stack g48">
    <div class="stack g12" style="max-width:640px"><p class="eyebrow">{dv["work_eyebrow"]}</p><h2>{dv["work_h"]}</h2></div>
    <article class="work">
      <div class="info"><span class="tag">{dv["work_tag"]}</span><h3 style="font-size:30px">{dv["work_name"]}</h3><p class="muted">{dv["work_p"]}</p><div class="feat">{feats}</div></div>
      <div class="shot" aria-hidden="true"><div class="mock"><div class="bar"><b></b><b></b><b></b></div><i style="width:60%"></i><i></i><i style="width:80%"></i><i style="width:45%"></i><i></i><i style="width:70%"></i></div></div>
    </article>
  </div>
</section>
'''
    mail = f"mailto:{EMAIL}?subject={dv['subject'].replace(' ', '%20')}"
    body = f'''<body>
{header(lang, d)}<main id="main">
<section class="page-hero">
  <div class="wrap stack g28">
    <nav class="crumbs" aria-label="{'مسار التصفح' if lang == 'ar' else 'Breadcrumb'}"><a href="{b}">{t["home_label"]}</a><span aria-hidden="true">/</span><a href="{b}#divisions">{t["nav"]["divisions"]}</a><span aria-hidden="true">/</span><span aria-current="page">{t["div_names"][d]}</span></nav>
    {ICONS[d]}
    <h1>{dv["h1"]}</h1>
    <p class="lead">{dv["lead"]}</p>
  </div>
</section>
<section>
  <div class="wrap stack g48">
    <h2>{dv["services_h"]}</h2>
    <div class="cards">{cards}</div>
  </div>
</section>
{work}<section class="{'' if d == 'technology' else 'alt'}">
  <div class="wrap" style="display:flex;flex-wrap:wrap;align-items:center;justify-content:space-between;gap:28px 48px">
    <div class="stack g12" style="max-width:640px"><h2>{dv["cta_h"]}</h2><p class="muted">{dv["cta_p"]}</p></div>
    <div class="btns"><a class="btn gold" href="{mail}">{dv["cta_btn"]}</a><a class="btn" href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a></div>
  </div>
</section>
</main>
{footer(lang)}<script src="/assets/js/main.js" defer></script>
</body></html>
'''
    return head(lang, d, dv["title"], dv["desc"], [crumb_ld(lang, d)]) + body

def privacy(lang):
    t = T[lang]; p = t["privacy"]; b = t["base"]
    paras = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in p["body"])
    body = f'''<body>
{header(lang, "privacy")}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><h1>{p["h1"]}</h1></div></section>
<section><div class="wrap prose">{paras}</div></section>
</main>
{footer(lang)}<script src="/assets/js/main.js" defer></script>
</body></html>
'''
    return head(lang, "privacy", p["title"], p["desc"], [crumb_ld(lang, "privacy")]) + body

def notfound():
    return '''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@600&family=IBM+Plex+Sans+Arabic:wght@300;400&display=swap">
<link rel="stylesheet" href="/assets/css/style.css"></head>
<body><main id="main" style="min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:40px 20px">
<div class="stack g20" style="align-items:center"><img src="/assets/img/mark.png" alt="" width="84" height="88">
<h1 style="font-size:44px">الصفحة غير موجودة</h1><p class="muted">Page not found</p>
<div class="btns" style="justify-content:center"><a class="btn gold" href="/">الرئيسية</a><a class="btn" href="/en/">Home (English)</a></div></div></main></body></html>
'''

def sitemap():
    keys = ["home"] + DIVS + ["privacy"]
    out = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ("ar", "en"):
        for k in keys:
            o = T[lang]["other"]
            out.append(f'<url><loc>{url(lang, k)}</loc>'
                       f'<xhtml:link rel="alternate" hreflang="{lang}" href="{url(lang, k)}"/>'
                       f'<xhtml:link rel="alternate" hreflang="{o}" href="{url(o, k)}"/>'
                       f'<xhtml:link rel="alternate" hreflang="x-default" href="{url("ar", k)}"/></url>')
    out.append("</urlset>")
    return "\n".join(out) + "\n"

if __name__ == "__main__":
    for lang in ("ar", "en"):
        b = T[lang]["base"].lstrip("/")
        write(f"{b}index.html", home(lang))
        for d in DIVS: write(f"{b}{d}/index.html", division(lang, d))
        write(f"{b}privacy/index.html", privacy(lang))
    write("404.html", notfound())
    write("sitemap.xml", sitemap())
    write("robots.txt", f"User-agent: *\nAllow: /\n\nSitemap: {SITE}/sitemap.xml\n")
    write("site.webmanifest", json.dumps({"name": "Alkarar Arrow | سهم الكرار", "short_name": "Alkarar Arrow", "start_url": "/", "display": "browser",
        "background_color": "#0b0b0d", "theme_color": "#0b0b0d",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; script-src 'self' 'unsafe-inline'; script-src-attr 'none'; base-uri 'self'; form-action 'self'; frame-ancestors 'none'; object-src 'none'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""")
    print("built")
