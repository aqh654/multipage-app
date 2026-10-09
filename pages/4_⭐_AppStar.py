import streamlit as st

st.set_page_config(page_title="AppStar", page_icon="⭐")

st.markdown("# AppStar ⭐")
st.sidebar.header("AppStar")
st.write(
    """A stellar life-cycle explorer built for 36104 Session 2 Part D.
Drag the mass, age and metallicity sliders to watch a star move across the
Hertzsprung-Russell diagram, from protostar through the main sequence to
giant, white dwarf, neutron star or black hole."""
)

st.link_button("Open AppStar", "https://star-app-blinkblink.streamlit.app")

st.markdown(
    """
    ### What it shows
    - **Main sequence:** hotter stars are brighter, and the band is coloured by black-body colour
    - **Giants and white dwarfs:** the star leaves the band up-right, then down-left
    - **Metallicity:** metal-poor stars burn out sooner, and below Z = 0.001 stars of
      140–260 suns undergo pair instability and leave no remnant
    """
)
