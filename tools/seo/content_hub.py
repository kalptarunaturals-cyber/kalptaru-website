# Category / concern page upgrades: t (title w/o brand), d, lead (replaces lead), guide (HTML), faq, links [(href-from-root, label)]
from content_ing import CLAYPOST, RETPOST, VCPOST
B = lambda s: f"blog/{s}.html"

CAT = {
"category/clays.html": dict(
 t="Cosmetic Clays Supplier in India – Amazonian Clays",
 d="Buy Brazilian Amazonian cosmetic clays in India: green, black, white, red, golden, purple and old rose kaolin clays from Bielus for masks and colour cosmetics.",
 lead="Seven naturally coloured Amazonian clays from Bielus, Brazil, for face masks, cleansers, scrubs and colour cosmetics. Kalptaru Naturals supplies samples, TDS and CoA across India.",
 guide="""<h2>Choosing an Amazonian clay</h2>
<p>Each Bielus clay takes its colour and character from its own minerals. Green and black clays are the most absorbent and suit oily skin and detox masks. White and old rose clays are the gentlest, for sensitive skin and powders. Red, golden and purple clays add striking natural colour from iron and manganese oxides, so a product can be tinted without synthetic dyes.</p>
<table><thead><tr><th>Clay</th><th>Character</th><th>Typical use</th></tr></thead><tbody>
<tr><td><a href="../ingredient/green-clay-amazon.html">Green Clay</a></td><td>Montmorillonite-rich, very absorbent</td><td>Purifying, oil-control masks</td></tr>
<tr><td><a href="../ingredient/black-clay.html">Black Clay</a></td><td>Smectite, illite, kaolinite; high adsorption</td><td>Detox masks, solid cleansers</td></tr>
<tr><td><a href="../ingredient/white-clay-from-the-amazon.html">White Clay</a></td><td>Gentle kaolin</td><td>Sensitive skin, powders</td></tr>
<tr><td><a href="../ingredient/old-rose-clay.html">Old Rose Clay</a></td><td>Mild iron-oxide pink</td><td>Soothing masks, blush</td></tr>
<tr><td><a href="../ingredient/red-clay.html">Red Clay</a></td><td>Hematite and goethite</td><td>Radiance masks</td></tr>
<tr><td><a href="../ingredient/golden-clay.html">Golden Clay</a></td><td>Kaolinite, illite, goethite</td><td>Brightening masks, warm tones</td></tr>
<tr><td><a href="../ingredient/purple-clay.html">Purple Clay</a></td><td>Manganese and iron chromophores</td><td>Statement masks, soaps</td></tr>
</tbody></table>
<p>Coloured clays are not designed to thicken. For a smooth, stable cream mask, pair them with a clay rheology modifier such as <a href="../ingredient/magnabrite-s.html">Magnabrite® S</a> or <a href="../ingredient/polargel-ca.html">Polargel® CA</a>.</p>""",
 faq=[("What are Amazonian clays used for?","Mainly in face and body masks, cleansers and scrubs, where they absorb oil and add natural colour."),
      ("Which clay is best for oily skin?","Green or black clay, the most absorbent in the Bielus range."),
      ("Which clay is best for sensitive skin?","White or old rose clay, the gentlest options."),
      ("Can I buy Amazonian clays in India?","Yes. Kalptaru Naturals is the Indian partner for Bielus and supplies samples, TDS and CoA.")],
 links=[(B(CLAYPOST),"Guide: Magnabrite®, Polargel® and Amazonian clays"),("concern/clays-and-masks.html","All clay and mask ingredients"),("category/rheology.html","Clay thickeners and stabilisers")]),
"concern/clays-and-masks.html": dict(
 t="Clay Mask Ingredients – Bentonite & Kaolin Clays India",
 d="Clay mask ingredients in India: Polargel® bentonites from HBS and Amazonian kaolin clays from Bielus for purifying, detox and soothing masks. Samples and TDS.",
 lead="Bentonites from HBS and coloured Amazonian clays from Bielus for face masks, cleansers and colour cosmetics: the base, the colour and the purifying claim in one place.",
 guide="""<h2>Building a clay mask</h2>
<p>Most clay masks combine two kinds of clay. A <strong>base clay</strong> such as <a href="../ingredient/polargel-ca.html">Polargel® CA</a> (calcium bentonite) gives body and carries high solids. A <strong>hero clay</strong> from the Bielus range, such as <a href="../ingredient/green-clay-amazon.html">green</a> or <a href="../ingredient/black-clay.html">black</a> clay for oily skin or <a href="../ingredient/white-clay-from-the-amazon.html">white</a> or <a href="../ingredient/old-rose-clay.html">old rose</a> for sensitive skin, provides the colour and the purifying or soothing story.</p>
<p>For creamy, wash-off masks that do not separate in the jar, add a little <a href="../ingredient/magnabrite-s.html">Magnabrite® S</a> or <a href="../ingredient/polargel-nf.html">Polargel® NF</a> to the water phase.</p>""",
 faq=[("What is the difference between bentonite and kaolin?","Bentonite is a swelling smectite clay that thickens and absorbs strongly; kaolin is gentler and absorbs less."),
      ("Which clay gives a mask its colour?","The Bielus Amazonian clays, which are coloured by natural minerals.")],
 links=[(B(CLAYPOST),"Guide: choosing the right cosmetic clay"),("category/clays.html","Amazonian clays"),("category/rheology.html","Clay thickeners")]),
"category/rheology.html": dict(
 t="Natural Clay Thickeners – Magnabrite®, Polargel® & More",
 d="Natural clay thickeners and emulsion stabilisers in India: Magnabrite® magnesium aluminium silicate, Polargel® bentonite, Volclay® and Hectabrite® from HBS.",
 lead="Mineral thickeners, suspending agents and emulsion stabilisers: Magnabrite® magnesium aluminium silicate, Polargel® and Volclay® bentonites and Hectabrite® hectorite from HBS (AMCOL), plus natural emulsifiers.",
 guide="""<h2>Which clay thickener?</h2>
<table><thead><tr><th>Grade</th><th>INCI</th><th>Viscosity at 5%</th><th>Choose it for</th></tr></thead><tbody>
<tr><td><a href="../ingredient/magnabrite-hv.html">Magnabrite® HV</a></td><td>Magnesium Aluminum Silicate</td><td>800–2200 cps</td><td>Most body at low dose</td></tr>
<tr><td><a href="../ingredient/magnabrite-s.html">Magnabrite® S</a></td><td>Magnesium Aluminum Silicate</td><td>225–600 cps</td><td>All-round, acid-tolerant</td></tr>
<tr><td><a href="../ingredient/magnabrite-f.html">Magnabrite® F</a></td><td>Magnesium Aluminum Silicate</td><td>150–450 cps</td><td>Powders, ointments</td></tr>
<tr><td><a href="../ingredient/magnabrite-k.html">Magnabrite® K</a></td><td>Magnesium Aluminum Silicate</td><td>100–300 cps</td><td>Acidic formulas</td></tr>
<tr><td><a href="../ingredient/magnabrite-hs.html">Magnabrite® HS</a></td><td>Magnesium Aluminum Silicate</td><td>40–200 cps</td><td>Electrolytes, hot or cold process</td></tr>
<tr><td><a href="../ingredient/polargel-hv.html">Polargel® HV</a></td><td>Bentonite</td><td>High</td><td>Roll-ons, rich creams</td></tr>
<tr><td><a href="../ingredient/polargel-nf.html">Polargel® NF</a></td><td>Bentonite</td><td>—</td><td>Make-up, AHA/BHA creams</td></tr>
<tr><td><a href="../ingredient/hectabrite-c.html">Hectabrite® C</a></td><td>Hectorite</td><td>High at low solids</td><td>Gels, strong shear thinning</td></tr>
</tbody></table>
<p>Magnabrite® viscosity ranges are from the HBS technical data sheets. Hydrate the clay in water under high shear before adding salts, glycols or actives, and pair it with xanthan gum for extra stability.</p>""",
 faq=[("What is magnesium aluminium silicate used for in cosmetics?","As a natural thickener, suspending agent and emulsion stabiliser in creams, lotions, sunscreens and masks."),
      ("Is Magnabrite an alternative to Veegum?","Both are magnesium aluminium silicate; Magnabrite® is the HBS (AMCOL) brand, with grades matched by viscosity and acid or electrolyte tolerance."),
      ("Are clay thickeners natural?","Yes. Magnabrite® and Polargel® are mined minerals, purified to USP/NF grade, with no animal or plant origin.")],
 links=[(B(CLAYPOST),"Guide: Magnabrite®, Polargel® and Amazonian clays"),("concern/texture-and-stability.html","Texture and stability ingredients"),("principal/hbs.html","All HBS / AMCOL ingredients")]),
"concern/texture-and-stability.html": dict(
 t="Texture & Stability Cosmetic Ingredients",
 d="Texture and stability ingredients in India: Magnabrite® and Polargel® clay thickeners, Polargel® UV SPF booster, PolyTrap® and Luxomatte® oil absorbers.",
 lead="Ingredients that shape how a product feels and keep it stable: clay thickeners, suspending agents, SPF boosters, oil absorbers and mattifying powders.",
 guide="""<h2>Texture and stability, by job</h2>
<ul><li><strong>Thicken and suspend:</strong> <a href="../ingredient/magnabrite-s.html">Magnabrite® S</a>, <a href="../ingredient/magnabrite-hv.html">Magnabrite® HV</a>, <a href="../ingredient/polargel-nf.html">Polargel® NF</a>, <a href="../ingredient/hectabrite-c.html">Hectabrite® C</a>.</li>
<li><strong>Boost SPF and reduce greasiness:</strong> <a href="../ingredient/polargel-uv.html">Polargel® UV</a> at 3–5%.</li>
<li><strong>Absorb oil and mattify:</strong> <a href="../ingredient/polytrap-pt-6603-oil-adsorber.html">PolyTrap® PT 6603</a> and <a href="../ingredient/luxomatte-n-mt125-mt128.html">Luxomatte® N MT125 / MT128</a>.</li></ul>""",
 faq=[("How do I stop a cream from separating?","Add a clay stabiliser such as Magnabrite® S or Polargel® NF, hydrated in the water phase, often with xanthan gum."),
      ("What is an SPF booster?","An ingredient such as Polargel® UV that raises measured SPF without adding more UV filters.")],
 links=[(B(CLAYPOST),"Guide: choosing a clay thickener"),("category/rheology.html","Emulsifiers, stabilisers and rheology")]),
"category/delivery.html": dict(
 t="Microsponge® Delivery Systems – Retinol & Vitamin C",
 d="Microsponge®, PolyPore® and PolyTrap® delivery systems from HBS in India: encapsulated retinol, retinaldehyde, vitamin C and acids. Samples and TDS.",
 lead="Encapsulated actives from HBS (AMCOL): Microsponge®, PolyPore® and PolyTrap® particles that protect retinol, retinaldehyde, vitamin C and acids and release them gradually on the skin.",
 guide="""<h2>Why use a delivery system?</h2>
<p>Many of the most effective actives are also the most fragile or irritating. Entrapping them in porous particles protects them from light and oxygen in the pack and releases them over time on the skin, which supports stability and tolerance.</p>
<ul><li><strong>Retinoids:</strong> <a href="../ingredient/microsponge-520ra-retinaldehyde.html">Microsponge® 520RA retinaldehyde</a>, <a href="../ingredient/microsponge-n-720tra.html">N 720TRA</a>, <a href="../ingredient/microsponge-c116a-retinol.html">C116A retinol</a>, <a href="../ingredient/microsponge-n-720tre.html">N 720TRE</a>, <a href="../ingredient/retinez.html">RetinEZ</a>. See the <a href="../topic/retinol-and-retinaldehyde.html">retinol and retinaldehyde guide</a>.</li>
<li><strong>Vitamin C:</strong> <a href="../ingredient/microsponge-n-720aa-vitamin-c.html">Microsponge® N 720AA</a> and <a href="../ingredient/microsponge-c133a-vitamin-c.html">C133A</a>. See the <a href="../topic/vitamin-c-ingredients.html">vitamin C guide</a>.</li>
<li><strong>Acids:</strong> <a href="../ingredient/microsponge-n-733sa-salicylic-acid.html">salicylic acid</a> and <a href="../ingredient/microsponge-n-725ga-glycolic-acid.html">glycolic acid</a> grades.</li></ul>""",
 faq=[("What is a Microsponge®?","A porous microparticle from HBS that holds an active and releases it gradually, used in cosmetic and prescription topical products."),
      ("What is the difference between Microsponge® and Microsponge® N?","Classic grades use an acrylate polymer; N grades use natural cellulose.")],
 links=[(B(RETPOST),"Guide: encapsulated retinaldehyde (Microsponge® 520RA)"),(B(VCPOST),"Guide: stable vitamin C serums"),("encapsulation.html","Custom encapsulation")]),
"concern/encapsulated-delivery.html": dict(
 t="Encapsulated Cosmetic Actives Supplier in India",
 d="Encapsulated cosmetic actives in India: Microsponge® retinol and retinal, ShellCare® vitamin C, liposomes and custom encapsulation from HBS, SCH, Nabsolute.",
 lead="Encapsulated retinol, retinaldehyde, vitamin C, tranexamic acid, peptides and more, from Microsponge® particles to polycaprolactone shells and targeted liposomes, plus custom encapsulation of your own active.",
 guide="""<h2>Encapsulation technologies we supply</h2>
<table><thead><tr><th>Technology</th><th>Principal</th><th>Best for</th></tr></thead><tbody>
<tr><td><a href="../category/delivery.html">Microsponge®, PolyPore®</a></td><td>HBS</td><td>Retinoids, vitamin C, acids; sustained release</td></tr>
<tr><td><a href="../category/nano.html">ShellCare® PCL nanocapsules</a></td><td>SCH</td><td>Vitamin C, tranexamic acid, niacinamide</td></tr>
<tr><td><a href="../ingredient/ziamozome-c.html">Ziamozome™ targeted liposomes</a></td><td>Nabsolute</td><td>Brightening actives for Asian skin</td></tr>
<tr><td><a href="../encapsulation.html">Custom encapsulation</a></td><td>SCH, HBS</td><td>Your own active, designed to brief</td></tr>
</tbody></table>
<p>Start with the <a href="../topic/retinol-and-retinaldehyde.html">retinol and retinaldehyde guide</a> or the <a href="../topic/vitamin-c-ingredients.html">vitamin C guide</a> to compare grades.</p>""",
 faq=[("Why encapsulate a cosmetic active?","To protect it from light, oxygen and water, mask odour or colour, and release it gradually to improve tolerance."),
      ("Can Kalptaru encapsulate my own active?","Yes. Through SCH and HBS we offer custom encapsulation from feasibility to scale-up.")],
 links=[("encapsulation.html","Custom encapsulation service"),(B(RETPOST),"Guide: encapsulated retinaldehyde"),(B(VCPOST),"Guide: stable vitamin C")]),
"category/nano.html": dict(
 t="Nano-Encapsulated Cosmetic Actives – SCH ShellCare®",
 d="Nano-encapsulated cosmetic actives in India: SCH ShellCare® polycaprolactone capsules for vitamin C, tranexamic acid, azelaic acid, niacinamide and more.",
 lead=None,
 guide="""<h2>About ShellCare® nanocapsules</h2>
<p>SCH ShellCare® actives are encapsulated in biodegradable polycaprolactone shells that shield sensitive molecules from water and oxygen and release them gradually. A good example is <a href="../ingredient/sch-shellcare-vit-c.html">ShellCare® Vit C</a>, which keeps L-ascorbic acid from turning a serum yellow.</p>""",
 faq=[("What is polycaprolactone?","A biodegradable polyester used to form the shells of SCH ShellCare® capsules.")],
 links=[(B(VCPOST),"Guide: stable vitamin C serums"),("encapsulation.html","Custom encapsulation")]),
"category/custom.html": dict(
 t="Custom Encapsulation Services – Liposomes, PCL & Alginate",
 d="Custom encapsulation of cosmetic actives in India: SCH polycaprolactone nanocapsules, tailored liposomes, alginate capsules and lipid-alginate hybrids.",
 lead=None,
 guide="""<h2>How custom encapsulation works</h2>
<p>Tell us the active, the format and the claim. SCH then chooses the shell (biodegradable polycaprolactone, liposome, alginate or a lipid-alginate hybrid), sets particle size and release, runs feasibility and scales up. See the <a href="../encapsulation.html">custom encapsulation page</a> for the full process.</p>""",
 faq=[("Which shell should I choose?","PCL for sustained release, liposomes for skin affinity, alginate for natural positioning and lip care, and the lipid-alginate hybrid for hydroalcoholic or light-sensitive products.")],
 links=[("encapsulation.html","Custom encapsulation service"),("concern/encapsulated-delivery.html","Ready-made encapsulated actives")]),
"concern/anti-ageing.html": dict(
 t=None, d=None, lead=None,
 guide="""<h2>Retinol and retinaldehyde for anti-ageing</h2>
<p>Retinoids remain the best-studied cosmetic anti-ageing actives. We supply encapsulated <a href="../ingredient/microsponge-520ra-retinaldehyde.html">retinaldehyde</a> and <a href="../ingredient/microsponge-n-720tre.html">retinol</a> in Microsponge® and PolyPore® carriers, <a href="../ingredient/retinez.html">RetinEZ</a> for easier manufacture and <a href="../ingredient/hbs-retinol-c50-ct50-ca50-cu50.html">50% liquid retinol</a>. Compare every grade in the <a href="../topic/retinol-and-retinaldehyde.html">retinol and retinaldehyde guide</a>.</p>""",
 faq=[], links=[(B(RETPOST),"Guide: encapsulated retinaldehyde"),("topic/retinol-and-retinaldehyde.html","Retinol and retinaldehyde ingredients")]),
"concern/brightening.html": dict(
 t=None, d=None, lead=None,
 guide="""<h2>Vitamin C for brightening</h2>
<p>Vitamin C brightens and protects, but pure L-ascorbic acid oxidises quickly. Our range covers encapsulated L-ascorbic acid (<a href="../ingredient/sch-shellcare-vit-c.html">ShellCare® Vit C</a>, <a href="../ingredient/microsponge-n-720aa-vitamin-c.html">Microsponge® N 720AA</a>), stable derivatives (<a href="../ingredient/sch-shellcare-vit-c-a.html">ethyl ascorbic acid</a>, <a href="../ingredient/sch-actives-map.html">MAP</a>) and a <a href="../ingredient/ziamozome-c.html">targeted liposome</a>. Compare them in the <a href="../topic/vitamin-c-ingredients.html">vitamin C guide</a>.</p>""",
 faq=[], links=[(B(VCPOST),"Guide: stable vitamin C serums"),("topic/vitamin-c-ingredients.html","Vitamin C ingredients")]),
"concern/antioxidant.html": dict(
 t=None, d=None, lead=None,
 guide="""<h2>Vitamin C antioxidants</h2>
<p>For antioxidant claims, compare encapsulated L-ascorbic acid, stable derivatives and gold-conjugated <a href="../ingredient/sch-actives-antiox-c.html">ascorbic and ferulic acid</a> in the <a href="../topic/vitamin-c-ingredients.html">vitamin C guide</a>.</p>""",
 faq=[], links=[(B(VCPOST),"Guide: stable vitamin C serums")]),
"encapsulation.html": dict(
 t=None,
 d=None, lead=None,
 guide="""<h2>Ready-made encapsulated actives</h2>
<p>Not every project needs a custom capsule. We also stock encapsulated <a href="topic/retinol-and-retinaldehyde.html">retinol and retinaldehyde</a>, <a href="topic/vitamin-c-ingredients.html">vitamin C</a>, tranexamic acid, niacinamide and acids in Microsponge®, PolyPore® and ShellCare® carriers. Browse them under <a href="concern/encapsulated-delivery.html">encapsulated delivery</a>.</p>""",
 faq=[("What is cosmetic encapsulation?","Enclosing an active inside a protective particle or vesicle to improve stability, mask colour or odour, and control release on the skin."),
      ("Which actives benefit most from encapsulation?","Unstable or irritating ones such as retinol, retinaldehyde, L-ascorbic acid and AHAs."),
      ("Do you offer custom encapsulation in India?","Yes. Kalptaru Naturals works with SCH, HBS and Nabsolute to encapsulate your active, from feasibility to scale-up.")],
 links=[(B(RETPOST),"Guide: encapsulated retinaldehyde"),(B(VCPOST),"Guide: stable vitamin C serums")]),
}

# ------------------------------------------------ new hub pages
HUBS = {
"topic/retinol-and-retinaldehyde.html": dict(
 t="Retinol & Retinaldehyde Ingredients Supplier in India",
 d="Encapsulated retinol and retinaldehyde for cosmetics in India: Microsponge®, PolyPore®, RetinEZ and 50% liquid retinol from HBS. Compare loads and carriers.",
 h1="Retinol and retinaldehyde ingredients",
 eyebrow="Topic guide · Retinoids",
 lead="Every retinoid grade we supply in India in one place: encapsulated retinaldehyde and retinol in acrylate or natural cellulose carriers, an easy-to-handle stabilised retinol and 50% liquid retinol.",
 ids=["microsponge-520ra-retinaldehyde","microsponge-n-720tra","microsponge-c116a-retinol","microsponge-n-720tre","microsponge-n-720re","microsponge-n-718tre-709re","polypore-120tre-120re-retinol","retinez","hbs-retinol-c50-ct50-ca50-cu50","sch-actives-reti-gold-c"],
 body="""<h2>Retinol or retinaldehyde?</h2>
<p>Skin converts retinoids to retinoic acid, the form that acts on skin cells. <strong>Retinol</strong> needs two oxidation steps to get there; <strong>retinaldehyde</strong> (retinal) needs one. Retinal therefore starts closer to the active form, while retinol is the most widely used and recognised name on pack. Both are sensitive to light and oxygen, which is why we focus on encapsulated grades.</p>
<h2>Compare the grades</h2>
<table><thead><tr><th>Grade</th><th>Retinoid</th><th>Load</th><th>Carrier</th><th>Notes</th></tr></thead><tbody>
<tr><td><a href="../ingredient/microsponge-520ra-retinaldehyde.html">Microsponge® 520RA</a></td><td>Retinaldehyde</td><td>20%</td><td>Acrylate</td><td>~0.5% gives 0.1% retinal; 44-week stability data</td></tr>
<tr><td><a href="../ingredient/microsponge-n-720tra.html">Microsponge® N 720TRA</a></td><td>Retinaldehyde</td><td>20%</td><td>Natural cellulose</td><td>8-week clinical: −13.2% fine lines</td></tr>
<tr><td><a href="../ingredient/microsponge-c116a-retinol.html">Microsponge® C116A</a></td><td>Retinol</td><td>23.5%</td><td>Acrylate</td><td>BHA-free</td></tr>
<tr><td><a href="../ingredient/microsponge-n-720tre.html">Microsponge® N 720TRE</a></td><td>Retinol + tocopherol</td><td>20%</td><td>Natural cellulose</td><td>BHA/BHT-free; 12-week wrinkle data</td></tr>
<tr><td><a href="../ingredient/microsponge-n-720re.html">Microsponge® N 720RE</a></td><td>Retinol</td><td>—</td><td>Natural cellulose</td><td>Clinical wrinkle reduction; body care</td></tr>
<tr><td><a href="../ingredient/microsponge-n-718tre-709re.html">Microsponge® N 718TRE / 709RE</a></td><td>Retinol</td><td>18% / 9%</td><td>Natural cellulose</td><td>Two strengths</td></tr>
<tr><td><a href="../ingredient/polypore-120tre-120re-retinol.html">PolyPore® 120TRE / 120RE</a></td><td>Retinol</td><td>20%</td><td>Allyl methacrylates crosspolymer</td><td>BHA/BHT-free options</td></tr>
<tr><td><a href="../ingredient/retinez.html">RetinEZ</a></td><td>Retinol</td><td>10%</td><td>Natural cellulose</td><td>No inert gas or yellow light needed</td></tr>
<tr><td><a href="../ingredient/hbs-retinol-c50-ct50-ca50-cu50.html">HBS Retinol C50 series</a></td><td>Retinol</td><td>50% liquid</td><td>None (free retinol)</td><td>BHA-, BHT-, polysorbate-free options</td></tr>
<tr><td><a href="../ingredient/sch-actives-reti-gold-c.html">SCH Reti Gold C</a></td><td>Retinol + gold, HA, peptide</td><td>Use at 0.3%</td><td>Gold conjugate</td><td>Premium multi-active</td></tr>
</tbody></table>
<h2>Formulating with retinoids</h2>
<ul><li>Add encapsulated retinoids in the cool-down phase, below the temperature on the TDS.</li>
<li>Minimise light and air: work under yellow light and use nitrogen where the TDS calls for it (RetinEZ is the exception).</li>
<li>Pack in airless pumps or laminate tubes.</li>
<li>Check the retinoid level you claim against the grade's loading; for example, 0.5% Microsponge® 520RA ≈ 0.1% retinal.</li></ul>""",
 faq=[("Is retinaldehyde better than retinol?","Retinaldehyde is one conversion step closer to retinoic acid. Which works better in a product depends on dose, formula and stability."),
      ("Why use encapsulated retinol?","Encapsulation protects retinol from light and oxygen and releases it gradually, supporting stability and lower irritation."),
      ("Do you have BHT-free retinol?","Yes. Microsponge® N 720TRE, PolyPore® options and some HBS Retinol 50 versions are BHA- and BHT-free."),
      ("Where can I buy retinol and retinaldehyde for cosmetics in India?","Kalptaru Naturals supplies HBS (AMCOL) and SCH retinoid grades across India with TDS, MSDS, CoA and samples.")],
 links=[(B(RETPOST),"Encapsulated retinaldehyde: Microsponge® 520RA data and formulation guide"),("concern/anti-ageing.html","All anti-ageing ingredients"),("category/delivery.html","Microsponge® delivery systems")]),
"topic/vitamin-c-ingredients.html": dict(
 t="Vitamin C Ingredients for Cosmetics – Supplier in India",
 d="Vitamin C ingredients for cosmetics in India: encapsulated L-ascorbic acid, ethyl ascorbic acid, MAP, Microsponge® and liposomal vitamin C. Compare grades.",
 h1="Vitamin C ingredients for cosmetics",
 eyebrow="Topic guide · Vitamin C",
 lead="Pure L-ascorbic acid is powerful but unstable. Compare the encapsulated forms, stable derivatives and conjugates we supply in India, and choose the right vitamin C for your serum or cream.",
 ids=["sch-shellcare-vit-c","microsponge-n-720aa-vitamin-c","microsponge-c133a-vitamin-c","sch-shellcare-vit-c-a","sch-actives-map","ziamozome-c","sch-actives-antiox-c"],
 body="""<h2>Why vitamin C serums turn yellow</h2>
<p>L-ascorbic acid oxidises when it meets water, oxygen, light and heat, turning a serum yellow then brown and losing activity. There are two ways round it: <strong>protect pure ascorbic acid</strong> inside a capsule or particle, or <strong>use a stable derivative</strong> that the skin can still use.</p>
<h2>Compare the grades</h2>
<table><thead><tr><th>Grade</th><th>Vitamin C form</th><th>Technology</th><th>Dose / load</th></tr></thead><tbody>
<tr><td><a href="../ingredient/sch-shellcare-vit-c.html">SCH ShellCare® Vit C</a></td><td>L-ascorbic acid</td><td>Polycaprolactone capsules</td><td>3–7%</td></tr>
<tr><td><a href="../ingredient/microsponge-n-720aa-vitamin-c.html">Microsponge® N 720AA</a></td><td>L-ascorbic acid</td><td>Natural cellulose microparticle</td><td>20% load</td></tr>
<tr><td><a href="../ingredient/microsponge-c133a-vitamin-c.html">Microsponge® C133A</a></td><td>L-ascorbic acid</td><td>Acrylate Microsponge®</td><td>50% load</td></tr>
<tr><td><a href="../ingredient/sch-shellcare-vit-c-a.html">SCH ShellCare® Vit C A</a></td><td>3-O-ethyl ascorbic acid</td><td>Stable derivative</td><td>1–5%</td></tr>
<tr><td><a href="../ingredient/sch-actives-map.html">SCH Actives™ MAP</a></td><td>Magnesium ascorbyl phosphate</td><td>Stable water-soluble derivative</td><td>—</td></tr>
<tr><td><a href="../ingredient/ziamozome-c.html">Ziamozome™ C</a></td><td>3-O-ethyl ascorbic acid + nonapeptide-1</td><td>Targeted liposome</td><td>—</td></tr>
<tr><td><a href="../ingredient/sch-actives-antiox-c.html">SCH Actives™ Antiox C</a></td><td>Ascorbic acid + ferulic acid</td><td>Gold conjugate</td><td>0.3–0.5%</td></tr>
</tbody></table>
<h2>Choosing a vitamin C</h2>
<ul><li><strong>"Pure vitamin C" claim:</strong> an encapsulated L-ascorbic acid such as ShellCare® Vit C or Microsponge® N 720AA.</li>
<li><strong>Pigmentation and melasma:</strong> ethyl ascorbic acid (ShellCare® Vit C A) or Ziamozome™ C.</li>
<li><strong>Easy, neutral-pH lotions:</strong> MAP.</li>
<li><strong>Antioxidant and anti-pollution:</strong> Antiox C with ferulic acid.</li></ul>""",
 faq=[("What is the most stable form of vitamin C for serums?","Stable derivatives such as 3-O-ethyl ascorbic acid and MAP, or L-ascorbic acid protected by encapsulation."),
      ("Does encapsulated vitamin C stop serums turning yellow?","Encapsulation slows the oxidation of L-ascorbic acid, which is what causes yellowing."),
      ("Where can I buy vitamin C ingredients for cosmetics in India?","Kalptaru Naturals supplies vitamin C grades from SCH, HBS and Nabsolute across India with TDS, CoA and samples.")],
 links=[(B(VCPOST),"Vitamin C serum with stable L-ascorbic acid: why it stops turning yellow"),("concern/brightening.html","All brightening ingredients"),("concern/antioxidant.html","All antioxidant ingredients")]),
}
