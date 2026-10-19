#!/usr/bin/env python3
"""Static site generator for Sahm Alkarar (Arabic + English).

Run `python3 build.py` after editing the content below. It rewrites every
HTML page, sitemap.xml and 404.html. No dependencies beyond Python 3.
"""
import json, os

import hashlib
def _v(p): return hashlib.md5(open(p,"rb").read()).hexdigest()[:8]
CSS="/assets/css/style.css?v="+_v("assets/css/style.css")
JS="/assets/js/main.js?v="+_v("assets/js/main.js")
SITE = "https://sahmalkarar.sa"
EMAIL = "info@sahmalkarar.sa"
PHONE_DISPLAY = "+966 50 020 9038"
PHONE_TEL = "+966500209038"
CR = "7050745707"
# Contact form delivery. Leave FORM_ENDPOINT empty to fall back to opening the visitor's email app.
# Formspree:  FORM_ENDPOINT = "https://formspree.io/f/xxxxxxxx"   (FORM_ACCESS_KEY stays empty)
# Web3Forms:  FORM_ENDPOINT = "https://api.web3forms.com/submit"  and  FORM_ACCESS_KEY = "<your access key>"
# Then run build.py and commit. The Content-Security-Policy in _headers already allows both services.
FORM_ENDPOINT = ""
FORM_ACCESS_KEY = ""
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
 "fonts": "https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@600;700&family=IBM+Plex+Sans+Arabic:wght@300;400;500;600;700&display=swap",
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
            "hq_val": "الرياض، حي العليا، 7854 سكاكا 12313",
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
   "work_eyebrow": "منتجاتنا", "work_h": "استقدام360: نظام إدارة الاستقدام",
   "work_tag": "منتج من سهم الكرار", "work_name": "استقدام360",
   "work_p": "نظام متكامل لإدارة عمليات الاستقدام، بُني من الصفر ليناسب طبيعة عمل شركات الاستقدام. يتابع العامل من توقيع العقد حتى الوصول، ويُبقي العميل على اطلاع بكل خطوة.",
   "prod_visit": "زيارة موقع استقدام360", "prod_url": "https://istiqdam360.netlify.app/", "prod_alt": "شعار استقدام360",
   "shot1_alt": "لوحة متابعة نظام إدارة الاستقدام تعرض مؤشرات العقود والعمالة", "shot2_alt": "شاشة إدارة العمالة في نظام الاستقدام مع الفلاتر والبحث", "shot_note": "لقطات من النظام، مع إخفاء البيانات الحقيقية.", "shot1_cap": "لوحة المتابعة", "shot2_cap": "إدارة العمالة", "open_full": "افتح الصورة كاملة",
   "work_feats": [("متابعة كاملة للعمالة", "من توقيع العقد حتى وصول العامل."),
                  ("تنبيهات تلقائية للعملاء", "رسائل نصية تصل العميل عند كل مرحلة."),
                  ("تطبيق للعميل", "يتابع العميل طلبه من جواله."),
                  ("بياناتك عندك", "يعمل على خادمك أو على خوادمنا."),
                  ("هوية شركتك", "مستندات وواجهات بشعار الشركة وألوانها.")],
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
  "effective": "تاريخ السريان: أكتوبر 2026",
  "body": [
   ("1. من نحن", "تُشغّل سهم الكرار (الرياض، المملكة العربية السعودية) هذا الموقع والخدمات المرتبطة به. وتشير عبارات «سهم الكرار» و«نحن» إلى هذه الجهة."),
   ("2. المعلومات التي نجمعها", "لا يجمع هذا الموقع بيانات شخصية من الزوار تلقائيًا، ولا يستخدم ملفات تعريف الارتباط. إذا راسلتنا عبر البريد الإلكتروني أو الهاتف، فإننا نستلم الاسم وجهة العمل وبيانات التواصل ومضمون استفسارك."),
   ("3. كيف نستخدم معلوماتك", "نستخدم المعلومات التي تصلنا للرد على استفسارك وتقييم فرص التعاون وحفظ سجل المراسلات المؤسسية. ولا نبيع بياناتك الشخصية ولا نؤجرها ولا نشاركها مع أطراف ثالثة لأغراض تسويقية."),
   ("4. مكان معالجة البيانات", "تُعالج البيانات التي تصلنا عبر هذا الموقع وفق متطلبات نظام حماية البيانات الشخصية (PDPL) وإرشادات الهيئة السعودية للبيانات والذكاء الاصطناعي (سدايا) المعمول بها."),
   ("5. حقوقك", "يحق لك طلب الاطلاع على بياناتك الشخصية أو تصحيحها أو حذفها أو تقييد معالجتها وفق الأنظمة المعمول بها. لممارسة هذه الحقوق تواصل معنا على " + EMAIL + "."),
   ("6. التواصل", "لأي استفسار عن الخصوصية راسلنا على " + EMAIL + "."),
  ]},
},
"en": {
 "dir": "ltr", "lang": "en", "base": "/en/", "other": "ar", "other_label": "العربية", "other_short": "عربي",
 "fonts": "https://fonts.googleapis.com/css2?family=Sora:wght@400;600;700&family=IBM+Plex+Sans:wght@300;400;500&display=swap",
 "brand": "Sahm Alkarar", "locale": "en_US", "other_locale": "ar_SA",
 "skip": "Skip to content",
 "nav": {"about": "About", "divisions": "Divisions", "contact": "Contact"},
 "home_label": "Home",
 "div_names": {"food": "Food", "technology": "Technology", "contracting": "Contracting"},
 "home": {
  "title": "Sahm Alkarar | Food, Technology and Contracting in Saudi Arabia",
  "desc": "Sahm Alkarar is a Saudi group based in Riyadh working in food, technology and contracting. We start with conviction, deliver with precision, and keep what we promise.",
  "eyebrow": "Riyadh · Saudi Arabia",
  "h1": "Boldness that hits the mark.",
  "lead": "A Saudi group working in food, technology and contracting. We start with conviction, deliver with precision, and keep what we promise.",
  "cta1": "Contact us", "cta2": "Our divisions",
  "logo_alt": "Sahm Alkarar logo",
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
            "hq_val": "Riyadh, Al Olaya, 7854 Sakaka 12313",
            "parent": "Parent company: Alexandria, Virginia, United States of America",
            "contact_h": "Contact", "div_h": "Divisions", "company_h": "Company", "privacy": "Privacy policy",
            "rights": "All rights reserved"},
 "divs": {
  "food": {
   "title": "Food | Sahm Alkarar",
   "desc": "Sahm Alkarar's food division: sourcing and trading of meat, sugar and staple food products for government and private clients in Saudi Arabia.",
   "short": "Sourcing and trading of food products with reliable quality and disciplined supply chains.",
   "bullets": ["Meat and food products", "Sugar and staple goods", "Supply to government and private sectors"],
   "h1": "Food",
   "lead": "We source and trade staple food products for government and private clients, with reliable quality and a disciplined supply chain.",
   "services_h": "What we offer",
   "services": [("Meat", "Lamb, goat, beef and poultry for restaurants, facilities and institutions."),
                ("Sugar and staples", "Supply of sugar and basic food goods in quantities that fit the client's need."),
                ("Supply to institutions", "Regular supply contracts for government bodies and companies, with clear delivery dates."),
                ("Quality and compliance", "We work to the requirements of the Kingdom's regulators and document each stage of supply.")],
   "cta_h": "Need food supply for your organization?", "cta_p": "Send us the items, quantities and date, and we will come back with a quotation.", "cta_btn": "Request a quotation",
   "subject": "Quotation request - Food division"},
  "technology": {
   "title": "Technology | Sahm Alkarar",
   "desc": "Sahm Alkarar's technology division: AI and business automation, IT and networking, cybersecurity and technology consulting, with a recruitment management system as previous work.",
   "short": "AI, IT and networking solutions, with technology consulting for organizations and companies.",
   "bullets": ["AI and business automation", "IT and networking", "Technology consulting"],
   "h1": "Technology",
   "lead": "We build technology that serves the work directly: AI and automation, infrastructure and networks, and custom systems designed around how the client operates.",
   "services_h": "What we offer",
   "services": [("AI and business automation", "Automating repetitive processes and building smart tools that save time and reduce errors."),
                ("IT and networking", "Network design, operation and support sized to the organization."),
                ("Cybersecurity", "Penetration testing, vulnerability assessment and security monitoring and operations."),
                ("Custom systems", "Systems built from scratch around the client's procedures, instead of bending the client to an off-the-shelf product."),
                ("Technology consulting", "Assessing the current state, setting priorities and a clear roadmap to execute.")],
   "work_eyebrow": "Our products", "work_h": "Istiqdam360: recruitment management system",
   "work_tag": "A product by Sahm Alkarar", "work_name": "Istiqdam360",
   "work_p": "An end-to-end system for managing recruitment operations, built from scratch around how recruitment companies work. It tracks each worker from contract signing to arrival and keeps the client informed at every step.",
   "prod_visit": "Visit the Istiqdam360 site", "prod_url": "https://istiqdam360.netlify.app/en/", "prod_alt": "Istiqdam360 logo",
   "shot1_alt": "Recruitment management system dashboard showing contract and worker indicators", "shot2_alt": "Workers management screen of the recruitment system with filters and search", "shot_note": "Screens from the system, with real data blurred.", "shot1_cap": "Tracking dashboard", "shot2_cap": "Workers management", "open_full": "open full size",
   "work_feats": [("Full worker tracking", "From contract signing to the worker's arrival."),
                  ("Automatic client alerts", "Text messages reach the client at every stage."),
                  ("Client mobile app", "Clients follow their order from their phone."),
                  ("Your data stays yours", "Runs on your own server or on ours."),
                  ("Your company's identity", "Documents and screens carry your logo and colors.")],
   "cta_h": "Have an idea or a system you need built?", "cta_p": "Tell us which process you want to simplify and we will propose the solution.", "cta_btn": "Discuss your project",
   "subject": "Inquiry - Technology division"},
  "contracting": {
   "title": "Contracting | Sahm Alkarar",
   "desc": "Sahm Alkarar's contracting division: general contracting, project management and execution, and maintenance and operations to clear quality and safety standards in Saudi Arabia.",
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
  "title": "Privacy policy | Sahm Alkarar",
  "desc": "How Sahm Alkarar handles the data it receives by email and through this website.",
  "h1": "Privacy policy",
  "effective": "Effective date: October 2026",
  "body": [
   ("1. Who we are", "Sahm Alkarar (Riyadh, Kingdom of Saudi Arabia) operates this website and related services. References to \"Sahm Alkarar\", \"we\" or \"our\" refer to this entity."),
   ("2. Information we collect", "This website does not collect personal data from visitors automatically and does not use cookies. If you contact us by email or phone, we receive your name, organization, contact details and the content of your inquiry."),
   ("3. How we use your information", "We use the information you send to respond to your inquiry, evaluate potential engagements and keep records of institutional communications. We do not sell, rent or share your personal data with third parties for marketing purposes."),
   ("4. Data residency", "Data received through this website is processed in accordance with the requirements of the Personal Data Protection Law (PDPL) and applicable SDAIA guidance."),
   ("5. Your rights", "You may have the right to access, correct, delete or restrict processing of your personal data under applicable law. To exercise these rights, contact us at " + EMAIL + "."),
   ("6. Contact", "For privacy inquiries, contact " + EMAIL + "."),
  ]},
},
}

FORM = {
 "ar": {"h": "أرسل لنا طلبك", "name": "الاسم", "org": "الجهة أو الشركة", "email": "البريد الإلكتروني", "phone": "الهاتف (اختياري)",
        "division": "القطاع", "msg": "تفاصيل طلبك", "msg_ph": "اكتب هنا ما تحتاجه: الأصناف والكميات، أو نطاق المشروع، أو الإجراء الذي تريد تبسيطه.",
        "consent": "أوافق على استخدام بياناتي للرد على طلبي وفق", "send": "إرسال الطلب", "sending": "جارٍ الإرسال...",
        "ok": "وصلنا طلبك، وسيعود إليك فريق القطاع المختص.", "err": "تعذر الإرسال. أرسل لنا على البريد مباشرة: " + EMAIL,
        "mail_note": "سيفتح الإرسال تطبيق البريد لديك برسالة جاهزة.", "other": "أخرى / غير محدد", "req": "هذا الحقل مطلوب",
        "subject": "طلب جديد من الموقع"},
 "en": {"h": "Send us your request", "name": "Name", "org": "Organization", "email": "Email", "phone": "Phone (optional)",
        "division": "Division", "msg": "Your request", "msg_ph": "Tell us what you need: items and quantities, the project scope, or the process you want to simplify.",
        "consent": "I agree that my data is used to answer my request, as described in the", "send": "Send request", "sending": "Sending...",
        "ok": "We received your request. The team for the right division will get back to you.", "err": "Could not send. Please email us directly: " + EMAIL,
        "mail_note": "Sending opens your email app with a ready message.", "other": "Other / not sure", "req": "This field is required",
        "subject": "New website request"},
}
PRODUCT_URL = {"ar": "https://istiqdam360.netlify.app/", "en": "https://istiqdam360.netlify.app/en/"}
PRODUCT_NAME = {"ar": "منتجنا: استقدام360", "en": "Our product: Istiqdam360"}
PRODUCT_BLURB = {"ar": "من تقنية سهم الكرار: نظام يدير الاستقدام من العقد حتى وصول العامل.", "en": "From Sahm Alkarar Technology: a system that runs recruitment from contract to arrival."}
PRODUCT_BTN = {"ar": "تعرّف على استقدام360", "en": "Explore Istiqdam360"}
LB = {"ar": "إغلاق", "en": "Close"}
MENU = {"ar": ("القائمة", "إغلاق القائمة"), "en": ("Menu", "Close menu")}
HOW = {
 "ar": {"h": "كيف نعمل", "food": [("الطلب", "تحدد الأصناف والكميات وموعد التوريد."), ("العرض", "نرسل لك عرضًا واضحًا بالأسعار والمواعيد."), ("التوريد", "ننفّذ التوريد وفق الاتفاق وبالجودة المطلوبة."), ("المتابعة", "نوثّق مراحل التوريد ونتابع معك بعد التسليم.")],
        "technology": [("فهم الإجراء", "نبدأ بفهم طريقة عملك والإجراء الذي تريد تبسيطه."), ("الحل المقترح", "نقترح حلًا وخطة وتكلفة قبل أي تنفيذ."), ("البناء والاختبار", "نبني الحل ونختبره معك على بيانات حقيقية."), ("التسليم والدعم", "نسلّم الحل وندرّب فريقك ونواصل الدعم.")],
        "contracting": [("دراسة النطاق", "نراجع نطاق العمل والموقع والمتطلبات."), ("العرض والجدول", "نقدّم عرضًا وجدولًا زمنيًا واضحًا."), ("التنفيذ", "ننفّذ ونتابع الجودة والسلامة والتكلفة."), ("التسليم", "نسلّم المشروع ونقدّم الصيانة والتشغيل عند الحاجة.")]},
 "en": {"h": "How we work", "food": [("Request", "You tell us the items, quantities and delivery date."), ("Quotation", "We send a clear quotation with prices and dates."), ("Supply", "We deliver as agreed, to the required quality."), ("Follow-up", "We document each stage and follow up after delivery.")],
        "technology": [("Understand the process", "We start by understanding how you work and what you want to simplify."), ("Proposed solution", "We propose a solution, plan and cost before any build."), ("Build and test", "We build it and test it with you on real data."), ("Handover and support", "We hand over, train your team and keep supporting it.")],
        "contracting": [("Scope review", "We review the scope of work, site and requirements."), ("Quotation and schedule", "We provide a quotation and a clear timeline."), ("Execution", "We deliver while tracking quality, safety and cost."), ("Handover", "We hand over the project and provide maintenance and operations when needed.")]},
}
FAQ = {
 "ar": {"h": "أسئلة شائعة",
  "food": [("هل تخدمون الجهات الحكومية؟", "نعم، نورّد للقطاعين الحكومي والخاص."), ("ما الذي أحتاجه لطلب عرض سعر؟", "أرسل لنا الأصناف والكميات وموعد التوريد المطلوب، ونعود إليك بعرض."), ("ما أنواع اللحوم المتوفرة؟", "نورّد لحوم الضأن والماعز والأبقار والدواجن.")],
  "technology": [("هل يمكن نشر النظام على خوادمنا؟", "نعم، يمكن نشر الأنظمة التي نبنيها داخل بيئتك لتبقى بياناتك عندك."), ("هل تبنون أنظمة من الصفر؟", "نعم، نبني الأنظمة حسب إجراءات العميل بدل تطويعه لنظام جاهز."), ("هل يظهر النظام بهوية شركتنا؟", "نعم، يقبل النظام شعار شركتك وألوانها ليظهر باسمك.")],
  "contracting": [("ما المعلومات اللازمة لعرض السعر؟", "نطاق العمل والموقع والموعد المطلوب، وأي مخططات أو متطلبات متوفرة."), ("هل تقدمون الصيانة بعد التسليم؟", "نعم، نقدّم عقود صيانة وتشغيل تبقي المنشأة جاهزة للعمل."), ("كيف تتعاملون مع السلامة والجودة؟", "نلتزم بإجراءات السلامة والجودة في كل موقع ونتابعها خلال التنفيذ.")]},
 "en": {"h": "Frequently asked questions",
  "food": [("Do you serve government bodies?", "Yes, we supply both government and private sector clients."), ("What do I need to request a quotation?", "Send us the items, quantities and the delivery date, and we will come back with a quotation."), ("Which meats do you supply?", "We supply lamb, goat, beef and poultry.")],
  "technology": [("Can the system be deployed on our own servers?", "Yes, the systems we build can be deployed inside your environment so your data stays with you."), ("Do you build systems from scratch?", "Yes. We build around the client's procedures instead of bending the client to an off-the-shelf product."), ("Can the system carry our branding?", "Yes. It takes your company's logo and colors so it appears under your name.")],
  "contracting": [("What do you need for a quotation?", "The scope of work, the site and the required date, plus any drawings or requirements you have."), ("Do you provide maintenance after handover?", "Yes, we offer maintenance and operating contracts that keep a facility ready for use."), ("How do you handle safety and quality?", "We follow safety and quality procedures on every site and track them during execution.")]},
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
<link rel="stylesheet" href="{CSS}">
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
  <button class="menu-btn" type="button" hidden aria-label="{MENU[lang][0]}" aria-expanded="false" aria-controls="site-nav" data-open="{MENU[lang][0]}" data-close="{MENU[lang][1]}"><span class="bars" aria-hidden="true"></span></button>
  <nav class="main" id="site-nav" aria-label="{'التنقل الرئيسي' if lang == 'ar' else 'Main'}">
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
      <li><a href="{PRODUCT_URL[lang]}" target="_blank" rel="noopener">{PRODUCT_NAME[lang]}</a></li>
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
    return {"@context": "https://schema.org", "@type": "Organization", "name": "Sahm Alkarar", "alternateName": "سهم الكرار",
            "url": SITE + "/", "logo": SITE + "/assets/img/icon-512.png", "email": EMAIL, "telephone": PHONE_TEL,
            "address": {"@type": "PostalAddress", "streetAddress": "7854 Sakaka, Al Olaya", "addressLocality": "Riyadh", "postalCode": "12313", "addressCountry": "SA"},
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
def form_html(lang, d=None):
    f = FORM[lang]; t = T[lang]
    opts = "".join(f'<option value="{k}"{" selected" if k == d else ""}>{t["div_names"][k]}</option>' for k in DIVS)
    opts += f'<option value=""{"" if d else " selected"}>{f["other"]}</option>' if not d else f'<option value="">{f["other"]}</option>'
    uid = "f-" + (d or "home")
    action = FORM_ENDPOINT or f"mailto:{EMAIL}"
    return f'''<form class="form" id="{uid}" method="post" action="{action}" data-endpoint="{FORM_ENDPOINT}" data-key="{FORM_ACCESS_KEY}" data-subject="{esc(f["subject"])}" data-ok="{esc(f["ok"])}" data-err="{esc(f["err"])}" data-sending="{esc(f["sending"])}" data-req="{esc(f["req"])}" novalidate>
  <h3>{f["h"]}</h3>
  <div class="fields">
    <label for="{uid}-name">{f["name"]}<input id="{uid}-name" name="name" type="text" autocomplete="name" required></label>
    <label for="{uid}-org">{f["org"]}<input id="{uid}-org" name="organization" type="text" autocomplete="organization"></label>
    <label for="{uid}-email">{f["email"]}<input id="{uid}-email" name="email" type="email" autocomplete="email" dir="ltr" required></label>
    <label for="{uid}-phone">{f["phone"]}<input id="{uid}-phone" name="phone" type="tel" autocomplete="tel" dir="ltr"></label>
    <label for="{uid}-div" class="full">{f["division"]}<select id="{uid}-div" name="division">{opts}</select></label>
    <label for="{uid}-msg" class="full">{f["msg"]}<textarea id="{uid}-msg" name="message" rows="5" placeholder="{esc(f["msg_ph"])}" required></textarea></label>
  </div>
  <input class="hp" type="text" name="_gotcha" tabindex="-1" autocomplete="off" aria-hidden="true">
  <label class="consent" for="{uid}-ok"><input id="{uid}-ok" name="consent" type="checkbox" required><span>{f["consent"]} <a href="{path_for(lang, "privacy")}">{t["labels"]["privacy"]}</a></span></label>
  <div class="actions"><button class="btn gold" type="submit">{f["send"]}</button>{'' if FORM_ENDPOINT else '<p class="note">' + f["mail_note"] + '</p>'}</div>
  <p class="status" role="status" aria-live="polite"></p>
</form>'''

def how_html(lang, d):
    steps = "".join(f'<li><span class="n" aria-hidden="true">{i + 1}</span><div><h3>{esc(a)}</h3><p>{esc(c)}</p></div></li>' for i, (a, c) in enumerate(HOW[lang][d]))
    return f'''<section id="how" class="alt"><div class="wrap stack g48"><h2>{HOW[lang]["h"]}</h2><ol class="steps">{steps}</ol></div></section>
'''

def faq_html(lang, d):
    items = "".join(f'<details><summary>{esc(q)}</summary><p>{esc(a)}</p></details>' for q, a in FAQ[lang][d])
    return f'''<section id="faq"><div class="wrap cols"><div class="stack g12"><h2>{FAQ[lang]["h"]}</h2></div><div class="faq">{items}</div></div></section>
'''

def faq_ld(lang, d):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in FAQ[lang][d]]}

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
    <div class="hero-art"><img src="{logo}" alt="{h["logo_alt"]}" width="440" height="{ '486' if lang == 'ar' else '397'}" fetchpriority="high"></div>
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
<section id="product">
  <div class="wrap">
    <div class="work"><div class="prod"><img src="/assets/img/istiqdam360-lockup.svg" alt="{T[lang]["divs"]["technology"]["prod_alt"]}" width="1400" height="440" loading="lazy"><div class="prod-side"><p>{PRODUCT_BLURB[lang]}</p><a class="btn gold" href="{path_for(lang, "technology")}#work">{PRODUCT_BTN[lang]}</a></div></div></div>
  </div>
</section>
<section id="contact" class="alt">
  <div class="wrap cols">
    <div class="stack g28"><div class="stack g20"><p class="eyebrow">{h["contact_eyebrow"]}</p><h2>{h["contact_h"]}</h2><p class="muted">{h["contact_p"]}</p></div>{contact_rows(lang)}</div>
    {form_html(lang)}
  </div>
</section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "home", h["title"], h["desc"], [org_ld(lang)]) + body

def division(lang, d):
    t = T[lang]; dv = t["divs"][d]; b = t["base"]
    cards = "".join(f'<div class="card"><h3 style="font-size:24px">{esc(a)}</h3><p style="margin-top:10px">{esc(c)}</p></div>' for a, c in dv["services"])
    work = ""
    if d == "technology":
        feats = "".join(f"<div><strong>{esc(a)}</strong><span>{esc(c)}</span></div>" for a, c in dv["work_feats"])
        work = f'''<section id="work">
  <div class="wrap stack g48">
    <div class="stack g12" style="max-width:640px"><p class="eyebrow">{dv["work_eyebrow"]}</p><h2>{dv["work_h"]}</h2></div>
    <article class="work">
      <div class="prod"><img src="/assets/img/istiqdam360-lockup.svg" alt="{esc(dv["prod_alt"])}" width="1400" height="440" loading="lazy"><div class="prod-side"><span class="tag">{dv["work_tag"]}</span><a class="btn gold" href="{dv["prod_url"]}" target="_blank" rel="noopener">{dv["prod_visit"]}</a></div></div>
      <div class="info"><div class="head"><h3 style="font-size:30px">{dv["work_name"]}</h3><p class="muted">{dv["work_p"]}</p></div><div class="feat">{feats}</div></div>
      <div class="shot">
        <ul class="shots">
          <li><figure><a class="win" href="/assets/img/work-dashboard.jpg" data-full="/assets/img/work-dashboard.jpg" target="_blank" rel="noopener" aria-label="{esc(dv["shot1_alt"])} ({dv["open_full"]})"><span class="bar" aria-hidden="true"><b></b><b></b><b></b></span><img src="/assets/img/work-dashboard.jpg" alt="{esc(dv["shot1_alt"])}" width="1200" height="590" loading="lazy"></a><figcaption>{dv["shot1_cap"]}</figcaption></figure></li>
          <li><figure><a class="win" href="/assets/img/work-workers.jpg" data-full="/assets/img/work-workers.jpg" target="_blank" rel="noopener" aria-label="{esc(dv["shot2_alt"])} ({dv["open_full"]})"><span class="bar" aria-hidden="true"><b></b><b></b><b></b></span><img src="/assets/img/work-workers.jpg" alt="{esc(dv["shot2_alt"])}" width="1200" height="590" loading="lazy"></a><figcaption>{dv["shot2_cap"]}</figcaption></figure></li>
        </ul>
        <p class="shot-note">{dv["shot_note"]}</p>
      </div>
    </article>
    <dialog class="lb" id="lightbox" aria-label="{LB[lang]}"><button class="lb-x" type="button" aria-label="{LB[lang]}"><span aria-hidden="true">&times;</span></button><img src="" alt="" width="1200" height="590"></dialog>
  </div>
</section>
'''
    mail = f"mailto:{EMAIL}?subject={dv['subject'].replace(' ', '%20')}"
    body = f'''<body>
{header(lang, d)}<main id="main">
<section class="page-hero">
  <div class="wrap cols" style="align-items:center">
    <div class="stack g28">
    <nav class="crumbs" aria-label="{'مسار التصفح' if lang == 'ar' else 'Breadcrumb'}"><a href="{b}">{t["home_label"]}</a><span aria-hidden="true">/</span><a href="{b}#divisions">{t["nav"]["divisions"]}</a><span aria-hidden="true">/</span><span aria-current="page">{t["div_names"][d]}</span></nav>
    <h1>{dv["h1"]}</h1>
    <p class="lead">{dv["lead"]}</p>
    </div>
    <div class="div-logo"><img src="/assets/img/div-{d}-{lang}.webp" alt="{'سهم الكرار - ' if lang == 'ar' else 'Sahm Alkarar - '}{t["div_names"][d]}" width="640" height="640" fetchpriority="high"></div>
  </div>
</section>
<section>
  <div class="wrap stack g48">
    <h2>{dv["services_h"]}</h2>
    <div class="cards">{cards}</div>
  </div>
</section>
{work}{how_html(lang, d)}{faq_html(lang, d)}<section id="request" class="alt">
  <div class="wrap cols">
    <div class="stack g28"><div class="stack g12"><h2>{dv["cta_h"]}</h2><p class="muted">{dv["cta_p"]}</p></div>
      <div class="btns"><a class="btn" href="tel:{PHONE_TEL}"><bdi>{PHONE_DISPLAY}</bdi></a><a class="btn" href="mailto:{EMAIL}"><bdi>{EMAIL}</bdi></a></div></div>
    {form_html(lang, d)}
  </div>
</section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, d, dv["title"], dv["desc"], [crumb_ld(lang, d), faq_ld(lang, d)]) + body

def privacy(lang):
    t = T[lang]; p = t["privacy"]; b = t["base"]
    paras = "".join(f"<h2>{a}</h2><p>{c}</p>" for a, c in p["body"])
    body = f'''<body>
{header(lang, "privacy")}<main id="main">
<section class="page-hero"><div class="wrap stack g20"><h1>{p["h1"]}</h1><p class="muted">{p["effective"]}</p></div></section>
<section><div class="wrap prose">{paras}</div></section>
</main>
{footer(lang)}<script src="{JS}" defer></script>
</body></html>
'''
    return head(lang, "privacy", p["title"], p["desc"], [crumb_ld(lang, "privacy")]) + body

def notfound():
    return f'''<!doctype html>
<html lang="ar" dir="rtl"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>الصفحة غير موجودة | Page not found</title><meta name="robots" content="noindex">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Reem+Kufi:wght@600&family=IBM+Plex+Sans+Arabic:wght@300;400&display=swap">
<link rel="stylesheet" href="{CSS}"></head>
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
    write("site.webmanifest", json.dumps({"name": "Sahm Alkarar | سهم الكرار", "short_name": "Sahm Alkarar", "start_url": "/", "display": "browser",
        "background_color": "#0b0b0d", "theme_color": "#0b0b0d",
        "icons": [{"src": "/assets/img/icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "/assets/img/icon-512.png", "sizes": "512x512", "type": "image/png"}]}, ensure_ascii=False, indent=2) + "\n")
    write("_headers", """/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: default-src 'self'; style-src 'self' https://fonts.googleapis.com; font-src https://fonts.gstatic.com; img-src 'self' data:; script-src 'self' 'unsafe-inline'; script-src-attr 'none'; base-uri 'self'; form-action 'self' mailto: https://formspree.io https://api.web3forms.com; connect-src 'self' https://formspree.io https://api.web3forms.com; frame-ancestors 'none'; object-src 'none'
/assets/*
  Cache-Control: public, max-age=31536000, immutable
""")
    print("built")
