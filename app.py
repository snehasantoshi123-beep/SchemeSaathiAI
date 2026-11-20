import streamlit as st

st.set_page_config(page_title="SchemeSaathi AI", page_icon="🇮🇳", layout="wide")

st.markdown("""
<style>
.stApp { background-color:#f3f7fc; color:#1f2937; }
.stApp p,.stApp h1,.stApp h2,.stApp h3,.stApp label,
div[data-testid="stMarkdownContainer"] { color:#1f2937 !important; }
.main-title { color:#123b70 !important; font-size:42px; font-weight:bold; text-align:center; }
.subtitle { color:#52677f !important; text-align:center; font-size:18px; }
.scheme-card { background:#fff; padding:18px; border-radius:14px; border:1px solid #dce6f2; min-height:160px; margin-bottom:8px; }
.scheme-card h3 { color:#174b85 !important; }
.scheme-card p { color:#46566a !important; font-size:15px; }
.stTextArea textarea { background:#fff !important; color:#1f2937 !important; border:1px solid #b8c9dc !important; border-radius:10px !important; }
.stTextArea textarea::placeholder { color:#718096 !important; }
.stButton button,[data-testid="stLinkButton"] a { background:#198754 !important; color:#fff !important; border:0 !important; border-radius:10px !important; font-weight:bold !important; }
.stButton button:hover,[data-testid="stLinkButton"] a:hover { background:#146c43 !important; color:#fff !important; }
.footer { text-align:center; color:#66788a !important; padding:25px; }
[data-testid="stSidebar"] { background:#e8f3ec !important; }
[data-testid="stSidebar"] h1,[data-testid="stSidebar"] h2,[data-testid="stSidebar"] h3,
[data-testid="stSidebar"] label,[data-testid="stSidebar"] p,[data-testid="stSidebar"] span {
 color:#174b35 !important; opacity:1 !important;
}
[data-testid="stSidebar"] [data-baseweb="select"] { background:#fff !important; border-radius:8px !important; }
[data-testid="stSidebar"] [data-baseweb="select"] div { color:#174b35 !important; }
[data-testid="stSidebar"] [data-baseweb="select"] > div { border-color:#198754 !important; }
[data-testid="stAlert"] {
    background-color: #e8f3ec !important;
    border: 1px solid #b7dfc5 !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] div,
[data-testid="stAlert"] span {
    color: #174b35 !important;
}
/* Note box visibility fix */
[data-testid="stAlert"],
[data-testid="stAlert"] > div {
    background-color: #e8f3ec !important;
    color: #174b35 !important;
    border: 1px solid #b7dfc5 !important;
}

[data-testid="stAlert"] p,
[data-testid="stAlert"] div,
[data-testid="stAlert"] span {
    color: #174b35 !important;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("⚙️ Settings")
language = st.sidebar.selectbox("Choose Language / భాష ఎంచుకోండి", ["English", "తెలుగు"])
te = language == "తెలుగు"

st.markdown('<div class="main-title">🇮🇳 SchemeSaathi AI</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your Personal Government Scheme Assistant</div>', unsafe_allow_html=True)
st.write("")
st.divider()

if te:
    st.subheader("స్వాగతం! 👋")
    st.write("మీ అవసరాలకు సరిపోయే ప్రభుత్వ పథకాల గురించి సులభమైన భాషలో తెలుసుకోండి.")
    question_label = "మీ పరిస్థితి గురించి వివరించండి"
    placeholder_text = "ఉదాహరణ: నేను రైతును. పంట బీమా లేదా ప్రభుత్వ సహాయం గురించి తెలుసుకోవాలి..."
    button_text = "🔍 తగిన పథకాలను కనుగొనండి"
else:
    st.subheader("Welcome! 👋")
    st.write("Discover government welfare schemes that may match your needs. Understand them in simple language.")
    question_label = "Describe your situation"
    placeholder_text = "Example: I am a farmer looking for crop insurance or government support..."
    button_text = "🔍 Find Suitable Schemes"

# This is a keyword-based demo matcher. It does not determine official eligibility.
schemes = [
    {
        "name":"🌾 PM-KISAN",
        "short_en":"Income support for eligible landholding farmer families.",
        "short_te":"అర్హత కలిగిన భూమి ఉన్న రైతు కుటుంబాలకు ఆదాయ సహాయం.",
        "benefit_en":"Provides ₹6,000 per year per eligible farmer family in three equal instalments, subject to scheme rules.",
        "benefit_te":"పథకం నిబంధనలకు లోబడి అర్హత కలిగిన రైతు కుటుంబానికి సంవత్సరానికి ₹6,000 మూడు విడతలుగా అందిస్తుంది.",
        "elig_en":"Cultivable land should be recorded in the farmer family's name. Exclusion rules apply.",
        "elig_te":"సాగుకు అనువైన భూమి రైతు కుటుంబం పేరుపై రికార్డులో ఉండాలి. మినహాయింపు నిబంధనలు వర్తిస్తాయి.",
        "docs_en":"Check Aadhaar, bank account details, land records and required e-KYC.",
        "docs_te":"ఆధార్, బ్యాంక్ ఖాతా వివరాలు, భూమి రికార్డులు మరియు అవసరమైన e-KYC వివరాలు తనిఖీ చేయండి.",
        "keywords":["farmer","farming","agriculture","farm","land","crop","రైతు","రైతులు","వ్యవసాయం","పంట","భూమి"],
        "link":"https://pmkisan.gov.in/"
    },
    {
        "name":"🏥 Ayushman Bharat PM-JAY",
        "short_en":"Hospitalisation health cover for eligible families.",
        "short_te":"అర్హత కలిగిన కుటుంబాలకు ఆసుపత్రి చికిత్స ఆరోగ్య కవరేజ్.",
        "benefit_en":"Offers cashless hospitalisation cover up to ₹5 lakh per eligible family per year at empanelled hospitals.",
        "benefit_te":"అనుబంధ ఆసుపత్రుల్లో అర్హత కలిగిన కుటుంబానికి సంవత్సరానికి ₹5 లక్షల వరకు నగదు రహిత చికిత్స కవరేజ్ అందిస్తుంది.",
        "elig_en":"Eligibility is based on government beneficiary criteria. Check your family in the official beneficiary portal.",
        "elig_te":"ప్రభుత్వ లబ్ధిదారుల ప్రమాణాల ఆధారంగా అర్హత నిర్ణయించబడుతుంది. అధికారిక పోర్టల్‌లో కుటుంబ వివరాలు తనిఖీ చేయండి.",
        "docs_en":"Keep Aadhaar or other accepted identity details and family/ration-card details available for verification.",
        "docs_te":"ధృవీకరణ కోసం ఆధార్ లేదా ఆమోదించిన గుర్తింపు వివరాలు, కుటుంబ/రేషన్ కార్డు వివరాలు సిద్ధంగా ఉంచండి.",
        "keywords":["health","hospital","medical","treatment","healthcare","sick","ఆరోగ్యం","ఆసుపత్రి","వైద్యం","చికిత్స","ఆరోగ్య బీమా"],
        "link":"https://beneficiary.nha.gov.in/"
    },
    {
        "name":"🔥 PM Ujjwala Yojana",
        "short_en":"LPG connection support for eligible adult women from poor households.",
        "short_te":"పేద కుటుంబాలకు చెందిన అర్హత కలిగిన వయోజన మహిళలకు LPG కనెక్షన్ సహాయం.",
        "benefit_en":"Provides a deposit-free LPG connection package under current scheme rules; applicable refill support should be checked on the official portal.",
        "benefit_te":"ప్రస్తుత పథకం నిబంధనల ప్రకారం డిపాజిట్ లేని LPG కనెక్షన్ ప్యాకేజీ అందిస్తుంది. రీఫిల్ సహాయాన్ని అధికారిక పోర్టల్‌లో తనిఖీ చేయండి.",
        "elig_en":"Applicant must be a woman aged 18 or above, from an eligible poor household, with no other household LPG connection.",
        "elig_te":"దరఖాస్తుదారు 18 ఏళ్లు లేదా అంతకంటే ఎక్కువ వయస్సు గల మహిళ అయి ఉండాలి; అర్హత కలిగిన పేద కుటుంబానికి చెందినవారై ఉండాలి; కుటుంబంలో ఇప్పటికే LPG కనెక్షన్ ఉండకూడదు.",
        "docs_en":"KYC, Aadhaar, ration card/family composition proof, bank details and prescribed declaration may be required.",
        "docs_te":"KYC, ఆధార్, రేషన్ కార్డు/కుటుంబ వివరాల పత్రం, బ్యాంక్ వివరాలు మరియు నిర్దేశిత ప్రకటన అవసరం కావచ్చు.",
        "keywords":["lpg","gas","cylinder","cooking gas","woman","women","గ్యాస్","మహిళ","మహిళలు","సిలిండర్","వంట గ్యాస్"],
        "link":"https://pmuy.gov.in/ujjwala2.html"
    },
    {
        "name":"🏠 Pradhan Mantri Awas Yojana",
        "short_en":"Housing assistance for eligible urban or rural households.",
        "short_te":"అర్హత కలిగిన పట్టణ లేదా గ్రామీణ కుటుంబాలకు గృహ సహాయం.",
        "benefit_en":"Supports eligible households to construct, purchase or access affordable housing through the applicable rural or urban component.",
        "benefit_te":"వర్తించే గ్రామీణ లేదా పట్టణ విభాగం ద్వారా అర్హత కలిగిన కుటుంబాలకు ఇల్లు నిర్మించుకోవడం, కొనుగోలు చేయడం లేదా అందుబాటు గృహం పొందడంలో సహాయం చేస్తుంది.",
        "elig_en":"Criteria differ between PMAY-Gramin and PMAY-Urban. Income, location, house ownership and prior housing assistance are considered.",
        "elig_te":"PMAY-గ్రామీణ, PMAY-పట్టణ పథకాల అర్హతలు వేర్వేరుగా ఉంటాయి. ఆదాయం, నివాస ప్రాంతం, ఇంటి యాజమాన్యం, గతంలో పొందిన గృహ సహాయం పరిగణనలోకి తీసుకుంటారు.",
        "docs_en":"Commonly check identity, residence, income, bank and household/house-ownership records. Exact documents vary by component and state.",
        "docs_te":"గుర్తింపు, నివాసం, ఆదాయం, బ్యాంక్ మరియు కుటుంబ/ఇంటి యాజమాన్య రికార్డులు తనిఖీ చేయండి. ఖచ్చితమైన పత్రాలు విభాగం, రాష్ట్రాన్ని బట్టి మారుతాయి.",
        "keywords":["house","home","housing","homeless","house construction","ఇల్లు","ఇంటి","గృహ","నివాసం","ఇల్లు నిర్మాణం"],
        "link":"https://pmay-urban.gov.in/"
    },
    {
        "name":"🛠️ PM Vishwakarma",
        "short_en":"Support for traditional artisans and craftspeople in notified trades.",
        "short_te":"నోటిఫై చేసిన సంప్రదాయ వృత్తుల చేతివృత్తిదారులకు సహాయం.",
        "benefit_en":"Includes recognition, skill support, toolkit incentive and access to collateral-free credit support, subject to scheme conditions.",
        "benefit_te":"పథకం నిబంధనలకు లోబడి గుర్తింపు, నైపుణ్య శిక్షణ, పనిముట్ల ప్రోత్సాహకం మరియు హామీ లేని రుణ సహాయం అందిస్తుంది.",
        "elig_en":"For eligible traditional artisans/craftspeople working with hands and tools in one of the notified family-based trades. Detailed conditions apply.",
        "elig_te":"నోటిఫై చేసిన కుటుంబ ఆధారిత సంప్రదాయ వృత్తుల్లో చేతులు, పనిముట్లతో పనిచేసే అర్హత కలిగిన చేతివృత్తిదారులకు. వివరమైన నిబంధనలు వర్తిస్తాయి.",
        "docs_en":"Aadhaar, mobile number, bank details and trade/occupation information may be needed during registration and verification.",
        "docs_te":"నమోదు, ధృవీకరణ సమయంలో ఆధార్, మొబైల్ నంబర్, బ్యాంక్ వివరాలు మరియు వృత్తి సమాచారం అవసరం కావచ్చు.",
        "keywords":["artisan","craft","carpenter","blacksmith","potter","tailor","mason","చేతివృత్తి","కమ్మరి","కుమ్మరి","వడ్రంగి","దర్జీ","కార్మికుడు"],
        "link":"https://pmvishwakarma.gov.in/"
    },
    {
        "name":"👧 Sukanya Samriddhi Yojana",
        "short_en":"Long-term savings account for the future of a girl child.",
        "short_te":"ఆడపిల్ల భవిష్యత్తు కోసం దీర్ఘకాలిక పొదుపు ఖాతా.",
        "benefit_en":"A guardian can open an account for an eligible girl child below 10 years; deposits earn government-notified interest.",
        "benefit_te":"10 సంవత్సరాల లోపు అర్హత కలిగిన ఆడపిల్ల పేరుతో సంరక్షకుడు ఖాతా తెరవవచ్చు; డిపాజిట్లపై ప్రభుత్వం ప్రకటించే వడ్డీ లభిస్తుంది.",
        "elig_en":"Account can be opened by a guardian in the name of a girl child who has not attained 10 years of age, subject to scheme rules.",
        "elig_te":"పథకం నిబంధనలకు లోబడి 10 సంవత్సరాల వయస్సు నిండని ఆడపిల్ల పేరుతో సంరక్షకుడు ఖాతా తెరవవచ్చు.",
        "docs_en":"Girl child's birth certificate and guardian's KYC/identity documents are required as per account-opening rules.",
        "docs_te":"ఖాతా ప్రారంభ నిబంధనల ప్రకారం ఆడపిల్ల జనన ధృవీకరణ పత్రం, సంరక్షకుడి KYC/గుర్తింపు పత్రాలు అవసరం.",
        "keywords":["girl child","daughter","girl","sukanya","education savings","ఆడపిల్ల","కూతురు","బాలిక","పాప","పొదుపు"],
        "link":"https://www.nsiindia.gov.in/"
    },
    {
        "name":"🏦 PM Jan Dhan Yojana",
        "short_en":"Access to basic banking services for people without a bank account.",
        "short_te":"బ్యాంకు ఖాతా లేని వారికి ప్రాథమిక బ్యాంకింగ్ సేవలు.",
        "benefit_en":"Offers a basic savings bank account with no minimum-balance requirement, RuPay card and access to eligible linked benefits.",
        "benefit_te":"కనీస నిల్వ అవసరం లేని ప్రాథమిక పొదుపు ఖాతా, RuPay కార్డు మరియు అర్హత ఆధారిత అనుబంధ ప్రయోజనాలకు అవకాశం కల్పిస్తుంది.",
        "elig_en":"People without a bank account can approach a bank branch or Bank Mitra; account and benefit conditions apply.",
        "elig_te":"బ్యాంకు ఖాతా లేని వారు బ్యాంకు శాఖ లేదా బ్యాంక్ మిత్రను సంప్రదించవచ్చు. ఖాతా, ప్రయోజనాలకు నిబంధనలు వర్తిస్తాయి.",
        "docs_en":"Aadhaar or other officially valid documents may be used as per bank KYC rules.",
        "docs_te":"బ్యాంకు KYC నిబంధనల ప్రకారం ఆధార్ లేదా ఇతర అధికారికంగా చెల్లుబాటు అయ్యే పత్రాలు ఉపయోగించవచ్చు.",
        "keywords":["bank account","banking","jan dhan","no bank","savings account","బ్యాంకు","బ్యాంక్ ఖాతా","జన్ ధన్","ఖాతా","పొదుపు ఖాతా"],
        "link":"https://www.pmjdy.gov.in/"
    },
    {
        "name":"💼 PM Mudra Yojana",
        "short_en":"Institutional loans for eligible micro and small business activities.",
        "short_te":"అర్హత కలిగిన సూక్ష్మ, చిన్న వ్యాపారాలకు సంస్థాగత రుణాలు.",
        "benefit_en":"Facilitates loans through lending institutions for eligible income-generating micro enterprises. Loan approval and terms depend on lender assessment.",
        "benefit_te":"ఆదాయం సృష్టించే అర్హత కలిగిన సూక్ష్మ వ్యాపారాలకు రుణ సంస్థల ద్వారా రుణ సదుపాయం కల్పిస్తుంది. ఆమోదం, నిబంధనలు రుణదాత పరిశీలనపై ఆధారపడి ఉంటాయి.",
        "elig_en":"Non-corporate, non-farm micro/small business activities may apply through participating lenders, subject to their requirements.",
        "elig_te":"పాల్గొనే రుణ సంస్థల ద్వారా వ్యవసాయేతర, కార్పొరేట్ కాని సూక్ష్మ/చిన్న వ్యాపార కార్యకలాపాలు దరఖాస్తు చేయవచ్చు. రుణదాత నిబంధనలు వర్తిస్తాయి.",
        "docs_en":"Business plan/details, identity, address, bank and business-related documents may be requested by the lender.",
        "docs_te":"వ్యాపార ప్రణాళిక/వివరాలు, గుర్తింపు, చిరునామా, బ్యాంక్ మరియు వ్యాపార సంబంధిత పత్రాలను రుణదాత అడగవచ్చు.",
        "keywords":["business","small business","shop","startup","entrepreneur","self employed","loan","వ్యాపారం","చిన్న వ్యాపారం","దుకాణం","స్వయం ఉపాధి","రుణం"],
        "link":"https://www.mudra.org.in/"
    },
    {
        "name":"🛒 PM SVANidhi",
        "short_en":"Working-capital loan support for eligible street vendors.",
        "short_te":"అర్హత కలిగిన వీధి వ్యాపారులకు వర్కింగ్ క్యాపిటల్ రుణ సహాయం.",
        "benefit_en":"Provides collateral-free working-capital loan support to eligible street vendors through participating lenders, under current guidelines.",
        "benefit_te":"ప్రస్తుత మార్గదర్శకాల ప్రకారం పాల్గొనే రుణ సంస్థల ద్వారా అర్హత కలిగిన వీధి వ్యాపారులకు హామీ లేని వర్కింగ్ క్యాపిటల్ రుణ సహాయం అందిస్తుంది.",
        "elig_en":"For eligible street vendors identified/verified under the scheme process by the urban local body or authorised process.",
        "elig_te":"పట్టణ స్థానిక సంస్థ లేదా అధీకృత ప్రక్రియ ద్వారా పథకం ప్రకారం గుర్తింపు/ధృవీకరణ పొందిన అర్హత కలిగిన వీధి వ్యాపారులకు.",
        "docs_en":"Vendor identification/certificate or Letter of Recommendation, identity and bank details may be needed as applicable.",
        "docs_te":"వర్తించే విధంగా విక్రేత గుర్తింపు/సర్టిఫికేట్ లేదా సిఫార్సు లేఖ, గుర్తింపు మరియు బ్యాంక్ వివరాలు అవసరం కావచ్చు.",
        "keywords":["street vendor","hawker","roadside seller","small vendor","cart","బండి","వీధి వ్యాపారి","చిరు వ్యాపారి","తోపుడు బండి","ఫుట్‌పాత్ వ్యాపారి"],
        "link":"https://pmsvanidhi.mohua.gov.in/"
    },
    {
        "name":"🌱 PM Fasal Bima Yojana",
        "short_en":"Crop insurance protection for notified crops and risks.",
        "short_te":"నోటిఫై చేసిన పంటలు, ప్రమాదాలకు పంట బీమా రక్షణ.",
        "benefit_en":"Provides insurance support against specified crop losses caused by notified non-preventable risks, subject to season and notification rules.",
        "benefit_te":"సీజన్, నోటిఫికేషన్ నిబంధనలకు లోబడి నివారించలేని నిర్దిష్ట ప్రమాదాల వల్ల పంట నష్టాలకు బీమా సహాయం అందిస్తుంది.",
        "elig_en":"Farmers cultivating notified crops in notified areas may enrol, subject to current state/season rules and insurable interest.",
        "elig_te":"నోటిఫై చేసిన ప్రాంతాల్లో నోటిఫై చేసిన పంటలు సాగు చేసే రైతులు, ప్రస్తుత రాష్ట్ర/సీజన్ నిబంధనలు మరియు బీమా అర్హతలకు లోబడి నమోదు చేసుకోవచ్చు.",
        "docs_en":"Aadhaar/identity, bank details, land or cultivation records and crop/area details may be required.",
        "docs_te":"ఆధార్/గుర్తింపు, బ్యాంక్ వివరాలు, భూమి లేదా సాగు రికార్డులు, పంట/విస్తీర్ణ వివరాలు అవసరం కావచ్చు.",
        "keywords":["crop insurance","crop loss","fasal","drought","flood","pest","పంట బీమా","పంట నష్టం","కరువు","వరద","తెగుళ్లు"],
        "link":"https://pmfby.gov.in/"
    }
    ,
    {
        "name":"👵 Atal Pension Yojana (APY)",
        "short_en":"A voluntary pension scheme for eligible Indian citizens planning for retirement.",
        "short_te":"పదవీ విరమణ తర్వాత ఆదాయం కోసం అర్హులైన భారతీయ పౌరుల స్వచ్ఛంద పెన్షన్ పథకం.",
        "benefit_en":"Provides a government-guaranteed minimum monthly pension after age 60, based on the contribution option selected.",
        "benefit_te":"ఎంచుకున్న చందా మొత్తాన్ని బట్టి 60 ఏళ్ల తర్వాత ప్రభుత్వం హామీ ఇచ్చే కనీస నెలవారీ పెన్షన్ అందిస్తుంది.",
        "elig_en":"Indian citizens aged 18–40 with a savings bank or post-office savings account may join. People who are or have been income-tax payers are not eligible to open a new APY account under the rule effective from 1 October 2022.",
        "elig_te":"18–40 ఏళ్ల భారతీయ పౌరులు పొదుపు బ్యాంక్ లేదా పోస్టాఫీస్ ఖాతాతో చేరవచ్చు. 1 అక్టోబర్ 2022 నుంచి అమల్లో ఉన్న నిబంధన ప్రకారం ఆదాయపు పన్ను చెల్లిస్తున్న లేదా గతంలో చెల్లించిన వారు కొత్త APY ఖాతా తెరవడానికి అర్హులు కారు.",
        "docs_en":"Savings bank/post-office account details, nominee details and KYC information as requested by the bank or post office.",
        "docs_te":"బ్యాంక్ లేదా పోస్టాఫీస్ అడిగే పొదుపు ఖాతా వివరాలు, నామినీ వివరాలు మరియు KYC సమాచారం.",
        "keywords":["atal pension","apy","pension","retirement","old age","monthly pension","పెన్షన్","వృద్ధాప్యం","విరమణ","పదవీ విరమణ"],
        "link":"https://pfrda.org.in/en/web/pfrda/schemes/atal-pension-yojana-apy"
    },
    {
        "name":"🛡️ PM Suraksha Bima Yojana (PMSBY)",
        "short_en":"Affordable personal accident insurance for eligible bank or post-office account holders.",
        "short_te":"అర్హత కలిగిన బ్యాంక్ లేదా పోస్టాఫీస్ ఖాతాదారులకు తక్కువ ప్రీమియంతో ప్రమాద బీమా.",
        "benefit_en":"Provides accident-related insurance cover: ₹2 lakh for accidental death or specified total disability and ₹1 lakh for specified partial disability, subject to policy terms. The listed annual premium is ₹20; verify the current premium before enrolment.",
        "benefit_te":"పాలసీ నిబంధనలకు లోబడి ప్రమాద మరణం లేదా నిర్దిష్ట పూర్తి వైకల్యానికి ₹2 లక్షలు, నిర్దిష్ట పాక్షిక వైకల్యానికి ₹1 లక్ష బీమా కవరేజ్ అందిస్తుంది. ప్రస్తుతం పేర్కొన్న వార్షిక ప్రీమియం ₹20; చేరే ముందు తాజా ప్రీమియాన్ని నిర్ధారించుకోండి.",
        "elig_en":"Generally available to participating bank/post-office account holders aged 18–70 who give consent for auto-debit. Check the latest scheme rules and premium with the bank.",
        "elig_te":"సాధారణంగా 18–70 ఏళ్ల మధ్య వయస్సు గల భాగస్వామ్య బ్యాంక్/పోస్టాఫీస్ ఖాతాదారులు ఆటో-డెబిట్‌కు సమ్మతి ఇచ్చి చేరవచ్చు. తాజా నిబంధనలు, ప్రీమియాన్ని బ్యాంక్ వద్ద నిర్ధారించుకోండి.",
        "docs_en":"Participating bank or post-office account details, consent/auto-debit authorisation and KYC details.",
        "docs_te":"భాగస్వామ్య బ్యాంక్ లేదా పోస్టాఫీస్ ఖాతా వివరాలు, సమ్మతి/ఆటో-డెబిట్ అనుమతి మరియు KYC వివరాలు.",
        "keywords":["pmsby","suraksha bima","accident insurance","accident cover","accidental","disability insurance","ప్రమాద బీమా","ప్రమాదం","వైకల్యం బీమా"],
        "link":"https://financialservices.gov.in/"
    },
    {
        "name":"❤️ PM Jeevan Jyoti Bima Yojana (PMJJBY)",
        "short_en":"Renewable one-year life insurance cover for eligible bank or post-office account holders.",
        "short_te":"అర్హత కలిగిన బ్యాంక్ లేదా పోస్టాఫీస్ ఖాతాదారులకు ప్రతి సంవత్సరం పునరుద్ధరించగల జీవిత బీమా.",
        "benefit_en":"Provides ₹2 lakh life cover for death due to any cause, subject to policy conditions. The listed annual premium is ₹436 and is collected by auto-debit; confirm the current premium and exclusions before joining.",
        "benefit_te":"పాలసీ నిబంధనలకు లోబడి ఏ కారణం వల్లైనా మరణిస్తే ₹2 లక్షల జీవిత బీమా కవరేజ్ అందిస్తుంది. పేర్కొన్న వార్షిక ప్రీమియం ₹436 ఆటో-డెబిట్ ద్వారా వసూలు చేస్తారు; చేరే ముందు తాజా ప్రీమియం, మినహాయింపులు నిర్ధారించుకోండి.",
        "elig_en":"Participating bank/post-office account holders aged 18–50 may enrol with auto-debit consent. A 30-day lien period applies to non-accidental death for first-time subscribers.",
        "elig_te":"18–50 ఏళ్ల మధ్య వయస్సు గల భాగస్వామ్య బ్యాంక్/పోస్టాఫీస్ ఖాతాదారులు ఆటో-డెబిట్ సమ్మతితో చేరవచ్చు. తొలిసారి చేరిన వారికి ప్రమాదేతర మరణాలపై 30 రోజుల లీన్ పీరియడ్ వర్తిస్తుంది.",
        "docs_en":"Savings bank/post-office account details, consent for auto-debit and KYC information.",
        "docs_te":"పొదుపు బ్యాంక్/పోస్టాఫీస్ ఖాతా వివరాలు, ఆటో-డెబిట్ సమ్మతి మరియు KYC సమాచారం.",
        "keywords":["pmjjby","jeevan jyoti","life insurance","life cover","death cover","జీవిత బీమా","జీవ బీమా","కుటుంబ భద్రత"],
                "link": "https://financialservices.gov.in/pmjjby",

    },
    {
        "name": "🎓 PM-USP Central Sector Scholarship",
        "short_en": "Scholarship support for meritorious students from economically weaker families.",
        "short_te": "ఆర్థికంగా వెనుకబడిన కుటుంబాలకు చెందిన ప్రతిభావంతులైన విద్యార్థులకు స్కాలర్‌షిప్.",
        "benefit_en": "Provides financial assistance for higher education to eligible students, subject to current scholarship guidelines.",
        "benefit_te": "ప్రస్తుత స్కాలర్‌షిప్ మార్గదర్శకాలకు లోబడి అర్హులైన విద్యార్థుల ఉన్నత విద్యకు ఆర్థిక సహాయం అందిస్తుంది.",
        "elig_en": "Students must meet the required Class 12 academic performance, family income and other eligibility conditions.",
        "elig_te": "విద్యార్థులు 12వ తరగతి మార్కులు, కుటుంబ ఆదాయం మరియు ఇతర అర్హత నిబంధనలను పాటించాలి.",
        "docs_en": "Class 12 marksheet, income certificate, bank details, Aadhaar and other documents required by the portal.",
        "docs_te": "12వ తరగతి మార్కుల జాబితా, ఆదాయ ధృవీకరణ పత్రం, బ్యాంక్ వివరాలు, ఆధార్ మరియు పోర్టల్ కోరిన ఇతర పత్రాలు.",
        "keywords": ["student", "scholarship", "college", "degree", "education", "tuition", "విద్యార్థి", "స్కాలర్‌షిప్", "కాలేజీ", "డిగ్రీ", "చదువు"],
        "link": "https://scholarships.gov.in/"
    },
    {
        "name": "👩‍🎓 AICTE Pragati Scholarship",
        "short_en": "Scholarship support for eligible girl students pursuing technical education.",
        "short_te": "సాంకేతిక విద్యను అభ్యసించే అర్హత కలిగిన బాలికలకు స్కాలర్‌షిప్ సహాయం.",
        "benefit_en": "Provides scholarship assistance to eligible girl students admitted to approved technical diploma or degree courses, subject to current AICTE rules.",
        "benefit_te": "ప్రస్తుత AICTE నిబంధనలకు లోబడి ఆమోదించబడిన సాంకేతిక డిప్లొమా లేదా డిగ్రీ కోర్సుల్లో చేరిన అర్హత కలిగిన బాలికలకు స్కాలర్‌షిప్ సహాయం అందిస్తుంది.",
        "elig_en": "For eligible girl students admitted to approved technical institutions. Family income and other AICTE conditions apply.",
        "elig_te": "ఆమోదించబడిన సాంకేతిక విద్యాసంస్థల్లో చేరిన అర్హత కలిగిన బాలికలకు. కుటుంబ ఆదాయం మరియు ఇతర AICTE నిబంధనలు వర్తిస్తాయి.",
        "docs_en": "Admission proof, previous academic marksheets, income certificate, Aadhaar and bank details may be required.",
        "docs_te": "ప్రవేశ ధృవీకరణ, గత విద్యా మార్కుల పత్రాలు, ఆదాయ ధృవీకరణ పత్రం, ఆధార్ మరియు బ్యాంక్ వివరాలు అవసరం కావచ్చు.",
        "keywords": ["pragati", "aicte", "girl student", "technical education", "engineering", "diploma", "బాలిక", "ఇంజనీరింగ్", "టెక్నికల్", "డిప్లొమా"],
        "link": "https://scholarships.gov.in/"
    }
]

# User input
user_text = st.text_area(
    question_label,
    placeholder=placeholder_text,
    height=120
)

if st.button(button_text, use_container_width=True):
    if user_text.strip():
        search_text = user_text.lower()

        matched_schemes = []
        for scheme in schemes:
            if any(keyword.lower() in search_text for keyword in scheme["keywords"]):
                matched_schemes.append(scheme)

        st.divider()

        if matched_schemes:
            if te:
                st.subheader("🎯 మీకు సరిపోయే పథకాలు")
            else:
                st.subheader("🎯 Suggested Government Schemes")

            for scheme in matched_schemes:
                with st.container():
                    st.markdown('<div class="scheme-card">', unsafe_allow_html=True)

                    st.markdown(f"### {scheme['name']}")

                    if te:
                        st.write(scheme["short_te"])
                        st.markdown("**ప్రయోజనాలు:**")
                        st.write(scheme["benefit_te"])
                        st.markdown("**అర్హత:**")
                        st.write(scheme["elig_te"])
                        st.markdown("**అవసరమైన పత్రాలు:**")
                        st.write(scheme["docs_te"])
                        st.link_button("🔗 అధికారిక వెబ్‌సైట్", scheme["link"])
                    else:
                        st.write(scheme["short_en"])
                        st.markdown("**Benefits:**")
                        st.write(scheme["benefit_en"])
                        st.markdown("**Eligibility:**")
                        st.write(scheme["elig_en"])
                        st.markdown("**Documents to check:**")
                        st.write(scheme["docs_en"])
                        st.link_button("🔗 Official Website", scheme["link"])

                    st.markdown("</div>", unsafe_allow_html=True)

        else:
            if te:
                st.warning("మీ వివరణకు సరిపోయే పథకం దొరకలేదు. వేరే పదాలతో మళ్లీ ప్రయత్నించండి.")
            else:
                st.warning("No matching scheme found. Try describing your situation with different keywords.")

    else:
        if te:
            st.warning("దయచేసి ముందుగా మీ పరిస్థితి గురించి వివరించండి.")
        else:
            st.warning("Please describe your situation first.")

# Explore all schemes
st.divider()

if te:
    st.header("🇮🇳 అన్ని ప్రభుత్వ పథకాలు")
    st.write("క్రింది 15 పథకాల గురించి తెలుసుకోండి.")
else:
    st.header("🇮🇳 Explore Government Schemes")
    st.write("Explore all 15 government schemes.")

columns = st.columns(3)

for index, scheme in enumerate(schemes):
    with columns[index % 3]:
        with st.expander(scheme["name"]):
            if te:
                st.write(scheme["short_te"])
                st.markdown("**ప్రయోజనాలు**")
                st.write(scheme["benefit_te"])
                st.markdown("**అర్హత**")
                st.write(scheme["elig_te"])
                st.markdown("**అవసరమైన పత్రాలు**")
                st.write(scheme["docs_te"])
                st.link_button("🔗 అధికారిక వెబ్‌సైట్", scheme["link"])
            else:
                st.write(scheme["short_en"])
                st.markdown("**Benefits**")
                st.write(scheme["benefit_en"])
                st.markdown("**Eligibility**")
                st.write(scheme["elig_en"])
                st.markdown("**Documents to check**")
                st.write(scheme["docs_en"])
                st.link_button("🔗 Official Website", scheme["link"])

st.divider()

if te:
    st.info("గమనిక: ఈ ప్రాజెక్ట్ కీవర్డ్ ఆధారంగా పథకాలను సూచించే డెమో. ఇది అధికారిక అర్హత నిర్ధారణ కాదు. తాజా నిబంధనలు, అర్హత మరియు దరఖాస్తు వివరాల కోసం అధికారిక వెబ్‌సైట్‌ను సందర్శించండి.")
    st.markdown('<div class="footer">🇮🇳 SchemeSaathi AI | ప్రజలకు ప్రభుత్వ పథకాలపై అవగాహన</div>', unsafe_allow_html=True)
else:
    st.info("Note: This project is a keyword-based demo matcher, not an official eligibility checker. Always verify current eligibility, benefits and application details on the official scheme website.")
    st.markdown('<div class="footer">🇮🇳 SchemeSaathi AI | Making Government Schemes Easier to Understand</div>', unsafe_allow_html=True)
