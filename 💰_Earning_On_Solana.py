import streamlit as st
from streamlit_extras.colored_header import colored_header

st.cache_data.clear()

st.set_page_config(
    page_title="Earning On Solana",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        "Get Help": None,
        "Report a bug": "https://twitter.com/tweb3girl",
        "About": None
    }
)

#style metric containers
st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: #c8d7db;
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: #b0020d;
}
</style>
"""
            , unsafe_allow_html=True)

st.markdown(f'<h1 style="color:#434346;font-size:60px;text-align:center;">{"Earning On Solana"}</h1>', unsafe_allow_html=True)

colored_header(
    label="",
    description="",
    color_name="gray-70",
)

st.warning('Your one-stop hub for earning in the Solana ecosystem! Discover diverse opportunities effortlessly. Explore now! 💰🚀')


st.header("General 🌐")
st.info('Diverse earning opportunities encompassing content creation, design, development, analysis, translations, and more.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://earn.superteam.fun">Superteam Earn</a></h1>', unsafe_allow_html=True)
st.markdown("""
Superteam Earn helps talent contribute to crypto projects through bounties and freelance gigs, in exchange for earning in crypto. Earning opportunities cut across content creation, design, development and analysis.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.stepdao.org/bounties">StepDAO Bounties</a></h1>', unsafe_allow_html=True)
st.markdown("""
StepDAO rewards active members within the Step community as well as users of the larger Solana ecosystem with $STEP tokens for completing bounties.

StepDAO offers a range of bounties across various categories, including Social Media, Translations, Developer Bounties, and Content Creation.
""")

st.markdown(f"<h1 style='font-size:22px;text-align:left;'><a href='https://deanslist.services/'>DEAN\'s List</a></h1>", unsafe_allow_html=True)
st.markdown("""
Dean's List enables people from around the world to work and earn using Web3 in the most decentralized way, on the Solana blockchain.

To unlock all these earning opportunities,  a Dean's List NFT is required, which is pretty rare these days. But not to worry, Dean's List has a [Business Visa program](https://visa.deanslist.services/) which allows anyone to apply for a 30 day trial to earn their way to an NFT.
""")


st.header("DePIN 🏗️")
st.info('Decentralized Physical Infrastructure Networks: earn crypto tokens through open, decentralized platforms for real-world infrastructure development.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://hivemapper.com/contribute">Hivemapper</a></h1>', unsafe_allow_html=True)
st.markdown("""
Hivemapper offers its $HONEY tokens to drivers who install a dashcam and collect mapping data as they drive around.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://know.rendernetwork.com/getting-started/what-role-am-i">Render Network</a></h1>', unsafe_allow_html=True)
st.markdown("""
Render allows anyone with excess GPU power to connect their hardware to its protocol and earn $RNDR by providing computing power for customer use cases such as machine learning training.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.helium.com/mine">Helium</a></h1>', unsafe_allow_html=True)
st.markdown("""
Helium enables distributed node runners to generate revenue by hosting dedicated hotspots from their homes or businesses to provide mobile connectivity to nearby users.
""")

st.header("Quests & Campaigns 📣")
st.info('Engage in rewarding quests and promotional activities to earn crypto tokens.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://beta.dequest.io/quests/">DeQuest</a></h1>', unsafe_allow_html=True)
st.markdown("""
Users can discover new games or learn skills by fulfilling quests or using new protocols - and get paid for that in crypto.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://taskon.xyz/">TaskOn</a></h1>', unsafe_allow_html=True)
st.markdown("""
TaskOn is a Web3 platform that brings users various web3 tasks in the form of reward campaigns, and rewards them with crypto on completion.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.okx.com/campaigns/solana-super-season">OKX Web3 Solana Super Season</a></h1>', unsafe_allow_html=True)
st.markdown("""
You can earn rewards while exploring the Solana Ecosystem with OKX. Explore different DApps and protocols and become a true SOL Maxi! The first wave has 120k USDT up for grabs.
""")


st.header("GameFi 🕹️")
st.info('Explore the intersection of gaming and finance, earning through in-game activities.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.genopets.me/">Genopets</a></h1>', unsafe_allow_html=True)
st.markdown("""
Genopets is a Web3 game that operates on a Move-To-Earn model, rewarding users with cryptocurrencies based on their physical activity.

You can also interact with other users, join quests, compete in battles, and participate in events for even more rewards.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.stepn.com/">StepN</a></h1>', unsafe_allow_html=True)
st.markdown("""
StepN is a Game-Fi project, where players with StepN NFTs can earn tokens through walking, jogging or running outdoors.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://aurory.io/">Aurory</a></h1>', unsafe_allow_html=True)
st.markdown("""
Aurory is a web3 game on Solana where active players can earn $AURY tokens, based on their in-game performance.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://ev.io/">ev.io</a></h1>', unsafe_allow_html=True)
st.markdown("""
ev.io is a first-person shooter game built on Solana which allows you to earn Solana for every kill. Players can use ev.io NFTs to upgrade weapons and player skins to increase earning power.
""")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://play.defiland.app/">Defi Land</a></h1>', unsafe_allow_html=True)
st.markdown("""
DeFi Land is a unique agriculture-simulation game created to gamify all aspects of decentralized finance. With specific NFTs players earn tokens for performing in-game activities like fishing, shooting, harvesting crops, and taking care of animals.
""")

st.header("Analytics 📈")
st.info('Monetize your analytical skills by participating in data analysis tasks and insights-driven projects.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://docs.flipsidecrypto.com/earn/analyst-rewards/top-30-dashboard-rewards">FlipsideCrypto Top 30</a></h1>', unsafe_allow_html=True)
st.markdown("""
Analyze Solana or other blockchain data on the Flipside app, publish and promote them, and if your dashboard spends time in the Top 30 trending dashboards you get paid by the hour.
""")

st.header("Writing ✍️")
st.info('Earn through your writing prowess, contributing content across various genres.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.bulbapp.io/write-to-earn">BULB</a></h1>', unsafe_allow_html=True)
st.markdown("""
BULB is a Web3 blogging platform with a unique 'Do-to-Earn' engagement model which incentivises writers and readers with tokens.

'BULBers' earn points for writing and engagement, and are rewarded with BULB tokens from the reward pool in proportion to their collected BULB points.
""")

st.header("Music 🎵")
st.info('Monetize your musical talent through music publishing, earning royalties and recognition for your compositions.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.ninaprotocol.com/">Nina Protocol</a></h1>', unsafe_allow_html=True)
st.markdown("""
Nina protocol is a platform with a decentralized file-distribution and tokenized ownership model, where independent artists can publish their music and always receive 100% of their sales given Nina takes no fees.
""")

st.header("Grants & Hackathons 🏆")
st.info('Secure funding through grants and showcase your skills in hackathons to earn rewards.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://x.com/0xmert_/status/1749198288513863700?s=46">Solana Scribes</a></h1>', unsafe_allow_html=True)
st.markdown("First-ever Solana hackathon for written content only.")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://solana.com/hackathon">Solana Hackathons</a></h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://www.encode.club/encodesolanahack">Encode Club Solana Hackathon</a></h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://solana.org/grants">Solana Grants</a></h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://li4rhd691jg.typeform.com/to/DOPVAt16">Dean’s list DecentraGrants</a></h1>', unsafe_allow_html=True)

st.header("Jobs 💼")
st.info('Traditional employment opportunities across a wide range of web3 companies and start-ups.', icon="ℹ️")

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://jobs.solana.com/jobs">Solana Job Board</a></h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://cryptojobslist.com/solana">Crypto Jobs List - Solana</a></h1>', unsafe_allow_html=True)

st.markdown(f'<h1 style="font-size:22px;text-align:left;"><a href="https://rethinkable.xyz/jobs">Rethinkable Jobs</a></h1>', unsafe_allow_html=True)
