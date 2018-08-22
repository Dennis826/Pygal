import pygal.maps.world

wm=pygal.maps.world.World()

wm.title="The Whole America"

wm.add("North America",{'ca':34126000,'us':309349000,'mx':113423000})
wm.add("Central America",["bz","cr","gt"])
wm.add("South America",["ar","bo","br"])

wm.render_to_file("America.svg")
