# importing  module
import os
import time
from google.cloud import asset_v1
from google.oauth2 import service_account

#ip_address to search
ip_address_to_find = input("Provide the ip address to find: ")

# handling auth for gcloud
SERVICE_ACCOUNT_KEY_FILE = "/path/to/your/service/account/key.json"

project_list = ["aamits-local", "aamits-mega-oqjmvq", "absolute-disk-279413", "ace-apex-197306", "adroit-dock-302603",
                "adsapicall", "adwordsashray", "ageless-welder-305315", "agent-c5613", "agent-name-4c44f",
                "agentchatbot-icue", "akhil10s1asdas", "alert-howl-351214", "alpha-nobroker-maps",
                "amplified-way-387009", "analytical-rig-400916", "analytics-demo-b507c", "ancient-lattice-244214",
                "annular-haven-310510", "api-5424054676975488169-425556", "api-access-for-python", "apollo-209110",
                "apollo-email-to-vendor", "app-46779605168781500335684739", "app-54054698589728825450092284",
                "app-81181327284852754517402195", "app-g52zurrg6kdufmohm3xahcnezu", "app-uninstall-track",
                "appscripts-378813", "arboreal-groove-340411", "arched-catwalk-354805", "arctic-marking-237412",
                "arshad-gsheet114441", "atomic-griffin-286708", "august-cirrus-399905", "autocomplete-1543560267172",
                "automation-triel", "autonomous-bit-369420", "avid-poet-362509", "baby-ylhtsy", "banking-iwqpbb",
                "beaming-might-400113", "bold-caldron-296616", "boxwood-mantra-283906", "brahmos-355ee",
                "braided-circuit-296605", "bridalflowers-26faa", "bubbly-clarity-382008", "bubbly-vine-230419",
                "builder-automati-1535983842573", "builder-projects", "builder-projects-247914",
                "burnished-timer-357510", "calcium-range-388611", "callcenter-345713", "callrecordings-226313",
                "callzen", "callzen-starship", "caramel-brook-392110", "card-tokenization-2", "causal-cacao-279011",
                "cb-welcome-glaytg", "cellular-cider-392908", "centered-pilot-400607", "charming-opus-388615",
                "chat-reply-through-email", "chatbot-listpage-search-sipn", "chatdemo-550ce", "chatdemo-a4733",
                "check-dialogflow-intent-danwqe", "checkout-peer", "checkout-starship", "chitchat-c7a19",
                "church-dashboard-1b21b", "circular-ether-302506", "clickearn-f77cb", "coffee-shop-kdtsqe",
                "composed-card-371810", "concise-cinema-392711", "concrete-sol-387707", "conductive-bot-393211",
                "cool-clarity-396919", "core-folio-375110", "core-silicon-305315", "cpmsservicing",
                "crack-talent-340018", "crucial-citron-332709", "cryptic-gate-283905", "cryptic-opus-400217",
                "cultivated-snow-355608", "curious-song-273018", "daring-pier-353016", "data-science-ml",
                "datafetch-379809", "decisive-cinema-267506", "deep-mechanism-384616", "deep-pursuit-370110",
                "delta-chess-284611", "demo5-b4239", "diesel-amulet-345210", "digital-gearing-325307",
                "direct-cocoa-391712", "discovertest", "discovertest-275111", "divine-camera-342212", "doorappconsumer",
                "drivedownload-283302", "drivetest-280810", "dulcet-palace-383312", "dummy-project-382012",
                "dump-download", "dumps-372113", "dynamic-poet-289309", "eco-rune-392806", "ecstatic-acumen-398908",
                "electric-facet-307717", "elegant-rock-353013", "elevated-agent-377808", "elite-anvil-399608",
                "elite-vista-239110", "emailsending1-357214", "emerald-entity-394011", "enduring-smile-394215",
                "eng-cache-397706", "eng-hash-268709", "engaged-rope-309321", "erudite-azimuth-304512",
                "esoteric-storm-379809", "evident-wind-312915", "extended-ascent-337207", "famous-analyzer-385506",
                "fast-audio-368305", "fastapp-ba7e8", "fcmtest-92bb4", "ferrous-amphora-293315",
                "ferrous-griffin-384011", "fiery-set-383012", "fine-program-335711", "fir-app-demo-c6f33",
                "fir-demo-f7d68", "fir-demo1-6f3e0", "fir-login-c602e", "first-tide-246207", "fluted-mercury-394011",
                "focal-column-387811", "focal-rampart-281106", "focal-shape-357808", "form-ae661",
                "formal-landing-382310", "formidable-deck-394011", "fresh-robot-398908", "friendlychat-4776c",
                "frmtracking", "ga-4-386721", "ga4-reporting-386610", "gam-project-fti-wk0-4sz",
                "genial-analogy-356207", "gentle-epoch-241507", "geodemo-ecb5b", "geospark-956df", "geostory-218c9",
                "gfacedetectionapp", "gold-circlet-397811", "golden-tide-237410", "grand-striker-360309",
                "graphic-chain-351313", "graphite-plane-376510", "green-orb-286707", "grounded-datum-326915",
                "gsheet-automation-318005", "gsheet-automation-399609", "gsheetapipython", "gtm-pc5pkhb-yty5m",
                "gtm-whsk59z5-yjizy", "hackathon-cc6fa", "handy-contact-345410", "hazel-env-253509",
                "helpful-aurora-285002", "hidden-brace-342309", "high-transit-395211", "home-store-app-7cbc1",
                "homeservice-bot", "hood-blackbox-2", "hood-device-automation", "hood-falcon", "hood-forum", "hood-ios",
                "hood-nova", "hood-nova1", "hood-nova2", "hood-nova3", "hood-role-assign-1608709759996",
                "hood-role-assign-1608709939944", "hood-securemeter", "hood-starship", "hoodforum", "hoodleads",
                "hopeful-vim-342307", "hs-prolance", "hypnotic-guard-345409", "i-mariner-290620",
                "iconic-medium-390908", "iconic-ruler-306307", "iconic-vine-372202", "imposing-quasar-381705",
                "inbound-augury-388510", "inbound-guru-374816", "india-land-1518568133136", "indigo-aurora-273210",
                "integral-plexus-369608", "intelligent-arc-388209", "interactions-1563866984186", "jovial-arch-280406",
                "jovial-opus-349303", "jovial-theory-194606", "jqdbejkdbcxec-pdci", "kalyani-project-381507",
                "keen-berm-278406", "keen-clarity-293105", "key-fabric-357508", "key-journal-194807",
                "kibana-auth-223313", "kishlay-merge-pdf", "kishlay-pdf-merge", "lead-project-381813",
                "leafy-bulwark-370420", "leafy-pilot-337207", "learndf-kibrek", "learning-gvio", "library-system-84d",
                "linear-reason-330307", "linen-marking-386414", "livepreviewfacedetectionapp", "local-20a82",
                "lockdown-leads", "long-sum-286807", "lucid-dynamo-387206", "lucky-trail-371505",
                "lunar-compiler-368407", "lustrous-center-307108", "macro-shore-367807", "magnetic-market-353307",
                "maps-prod-v1", "massive-tea-396919", "master-magnet-333910", "maximal-grin-306111",
                "melodic-furnace-370112", "midyear-spot-398506", "mlkitsample-c40c6", "model-axle-312911",
                "modular-ethos-279319", "my-project-1519373559976", "my-project-1536039720383",
                "my-project-1536909910812", "my-project-1541825640551", "my-project-1547806444663",
                "my-project-1563521156280", "my-project-1567499801772", "my-project-1575534979488",
                "my-project-1638439048899", "my-project-2-1528719050446", "my-project-372205", "my-project-8315-205510",
                "my-project-auto1-394613", "my-projectbb-blo-1577204181841", "my-projects-357507",
                "my-projectsample-327604", "mystical-sphinx-384105", "n007-sakvqj", "nb-bbps-core", "nb-crm",
                "nb-movers-and-packers", "nb-outbound", "nb-partner-stage1", "nb-pg-328110", "nb-test-project-255508",
                "nb-unified", "nbdev-207009", "nbformelement", "nbh-insights-sales", "nbplanchat-utmw", "nbrmfield",
                "neat-axis-252507", "neat-dispatch-363308", "never-never-271611", "newagent-d7e31", "newagent-fodm",
                "newagent-uqeiqy", "nice-dispatcher-365111", "nifty-artwork-209109", "nimble-augury-310812",
                "nimble-willow-379311", "ninth-tensor-342306", "no-broker", "no-broker-developer", "nob-bigquery",
                "nob-blackbox", "nob-blackbox-2", "nob-buzzbroker", "nob-chatbot", "nob-chatbot-welcome-bgfjnq",
                "nob-database", "nob-email-netcore", "nob-falcon", "nob-gcp-monitoring", "nob-homeservices",
                "nob-kubernetes", "nob-mongodb", "nob-nobroker1", "nob-nobroker2", "nob-nobroker3", "nob-p2p",
                "nob-platform", "nob-sandbox", "nob-sap-b1-stage", "nob-secure", "nob-servicing", "nob-starship",
                "nob-supernova-261617", "nob-taskpane", "nob-uniview", "nob-watchdog", "nob-whatsapp", "nobr-test",
                "nobroker-199315", "nobroker-360509", "nobroker-botify-1619757513778", "nobroker-callzen-public",
                "nobroker-chatbot-prod", "nobroker-chatbot-stage-hkydst", "nobroker-checkout", "nobroker-frontend-prod",
                "nobroker-hood-testing", "nobroker-lead-1537253525414", "nobroker-local",
                "nobroker-local-1521616086198", "nobroker-public", "nobroker-public-394115", "nobroker-sap-b1",
                "nobroker-stage", "nobroker-stage-285610", "nobroker-uplift", "nobrokergroup",
                "nobrokerhood-anciliary-sevices", "nobrokerhood-gtm", "nobrokerhood-in", "nobrokerhood-stage",
                "nobrokernotification", "nobrokertest-f9c26", "nodal-operand-382112", "notification-master-eaeaf",
                "notificationexample-12cc4", "nps-developer-345410", "onyx-inn-377210", "optimum-library-359608",
                "organic-storm-280016", "osvcl-340707", "our-chess-400107", "oyo-intr", "pack-and-store",
                "pagespeed-205510", "payment-routing", "personalapp-32fae", "pivotal-crawler-338720",
                "pivotal-pattern-332317", "pnm-chatbot-nl9n", "poc1-214306", "polar-avenue-399808",
                "precise-valor-301409", "prefab-mapper-390609", "premium-modem-386415", "primal-context-384203",
                "prime-phalanx-337806", "principal-storm-373711", "probable-lore-289307", "project-x-224fd",
                "project-x-9a240", "projectinsight-398107", "projectmis", "propertyselect-mpud",
                "protean-sensor-357506", "proud-cathode-382413", "python-connect-382112", "quick-processor-386913",
                "quickstart-1549972274125", "quickstart-1561990974791", "quickstart-1562048592238",
                "quickstart-1569320906676", "quickstart-1569320948630", "quickstart-1569320984958",
                "quickstart-1583992778583", "quickstart-1591334750879", "quickstart-1591861013081",
                "quickstart-1592545084222", "quickstart-1592545088264", "quickstart-1609211650749",
                "quickstart-1643797284371", "quickstart-1646051185610", "quickstart-1681121691547",
                "quixotic-spot-391303", "radar-demo-214306", "rare-haiku-280007", "rare-haiku-281516",
                "reactmaps-358713", "red-abstraction-327508", "red-reference-289309", "remoteuidemo",
                "rentalagreement-ueem", "rentvsbuy-1530866310896", "report-b1677", "restro-ec23e",
                "reverberant-yew-274216", "reviewclassifier-e7411", "reviewsubteamclassifier",
                "reviewsubteamclassifier-51746", "reviewsubteamclassifier-5da51", "reviewsubteamclassifier-acc2e",
                "reviewsubteamclassifier-aeae4", "river-nectar-398812", "river-tiger-258805", "roommmate-matching",
                "rugged-diagram-378019", "sage-webbing-285116", "samir-at-nb", "search-location-and-get-type",
                "secret-argon-360210", "secure-bolt-394011", "seller-pitch", "seraphic-amp-307717",
                "seraphic-music-285116", "serious-amp-273803", "serious-amulet-386405", "shlok-gxfy", "shorturl-1119",
                "singular-arcana-297908", "sinuous-moment-400916", "skilled-bee-353910", "slashrtc-199606",
                "smartsearch-bot", "smooth-tesla-195410", "southern-silo-368408", "soy-meridian-203011",
                "spartan-calling-195712", "spartan-network-370112", "speedy-league-370108", "spheric-brand-372212",
                "spherical-realm-267510", "spiritual-oxide-275110", "spiritual-pride-337312", "spreadsheet-poc-385507",
                "spry-sensor-392610", "srinivas-testing", "starship-impost", "stayeasy-191506", "stayeasy-local",
                "steady-grid-345215", "steam-insight-375005", "steam-treat-293512", "steel-index-350507",
                "steel-sequencer-291013", "steganos-20180926", "stoked-bivouac-381211", "stoked-magpie-255406",
                "stone-resource-392110", "strong-hue-390312", "studied-groove-354307", "stunning-crane-390908",
                "sublime-cargo-291412", "summer-optics-286907", "sunlit-precinct-240010", "swift-sphinx-265116",
                "tars-pxuxvd", "tasks-widget", "teak-kit-357107", "teak-proton-356410", "tech-issues-hs",
                "tenacious-coder-265806", "tensile-talent-392715", "test-4828b", "test-bot-amdg", "test-btqv",
                "test-chat-func", "test-euqx", "test-ga-2-340109", "test-ga-340106", "test-oyo", "test2-rwsg",
                "testing-qawj", "testingfirebase-bf202", "testproject-384616", "testscheduler-eroq", "third-pad-290912",
                "tidy-hold-274216", "titanium-deck-303408", "totemic-fulcrum-302407", "track-app-uninstall",
                "track-app-uninstall-200611", "tribal-saga-368407", "trim-mote-369305", "triple-name-315413",
                "ultimate-figure-326517", "unified-radar-386913", "united-time-205510", "uniview-14b05",
                "uniview-1b43f", "uniview-ab91a", "uniview-b29fb", "uniview-starship", "univieworganisation",
                "univiewtest", "univiewtest-277309", "unsubscribe-uvmi", "upbeat-math-317106", "uplifted-sphinx-270111",
                "useful-gearbox-280506", "utilitarian-bee-342006", "v-lookup-396919", "valid-cell-301506",
                "valid-hall-295212", "vendor-1578387323035", "vigilant-art-399808", "virtual-muse-270912",
                "voltaic-cairn-382109", "watchful-hall-333917", "water-hood", "weighty-beach-388611",
                "western-avatar-392806", "whatsapp-chatbot-341414", "whatsapp-cloud-function", "white-airship-297506",
                "white-position-289512", "white-terra-274707", "winged-octagon-375519", "youtube-api-demo-353607",
                "zinc-chiller-270011", "zinc-fusion-268305"]

# Authenticate with service account
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_FILE)


# function to check if the ip address exist in the project
def check_ip_in_project(project_id, ip_address):
    client = asset_v1.AssetServiceClient()
    query = f'''(
            resourceProperties.networkInterfaces.accessConfigs.natIP="*{ip_address}*" OR 
            resourceProperties.networkInterfaces.accessConfigs.externalIp="*{ip_address}*" OR
            resourceProperties.networkInterfaces.networkIP="*{ip_address}*" OR
            resourceProperties.services.clusterIP="*{ip_address}*" OR
            resourceProperties.services.loadBalancerIP="*{ip_address}*" OR
            resourceProperties.ingresses.ip="*{ip_address}*" OR
            resourceProperties.k8s_pod.ip="*{ip_address}*"
    )'''
    # setting up project scope
    scope = f"projects/{project_id}"

    # make the asset API request
    assets = client.search_all_resources(scope=scope, query=query)
    for result in assets:
        print(f"Project Name: {result.asset.resource.project_display_name}")
        print(f"Resource Name: {result.asset.resource.name}")

    return any(assets)


# looping through the project list
for project_id in project_list:
    try:
        if check_ip_in_project(project_id=project_id, ip_address=ip_address_to_find):
            print(f"IP-address found in the project {project_id}")

    except Exception as e:
        print(f"Error checking project {project_id}: {str(e)}")
