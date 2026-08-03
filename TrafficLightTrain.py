import carb
import omni.replicator.core as rep

settings = carb.settings.get_settings()
settings.set("/rtx/post/denoiser/enabled", False)
settings.set("/rtx/post/aa/op", 0)  # 0=None, 1=FXAA, etc.

with rep.new_layer():
    map = rep.get.prims(path_pattern="/Root/Map", prim_types=['Xform'])
    sun = rep.get.prims(path_pattern="/Root/DistantLight", prim_types=['DistantLight'])

    currentLight = None    

    camera = rep.create.camera(position=(5.0, 0, 0.3183), look_at=(0, 0, 0.3))
    render_product = rep.create.render_product(camera, (560, 560))

    def randomizeSun():   
        with sun:
            rep.modify.pose(position=(0, 0, 0), rotation=rep.distribution.uniform((-40, 0, -180), (-20, 0, 180)))
                    
        return sun.node
 
    def randomizeRedLight():
        red = rep.get.prims(path_pattern="/Root/_001001/combined_solid_red_0", prim_types=['Xform'])
        with red:
            rep.modify.visibility(rep.distribution.choice([True, False]))
            # rep.modify.semantics([("class", "red")], mode="replace") 
        return red.node
    
    def randomizeYellowLight(): 
        yellow = rep.get.prims(path_pattern="/Root/_001001/combined_solid_yellow_1", prim_types=['Xform'])
        with yellow:
            rep.modify.visibility(rep.distribution.choice([True, False])) 
            # rep.modify.semantics([("class", "yellow")], mode="replace")
        return yellow.node 
    
    def randomizeGreenLight():
        green = rep.get.prims(path_pattern="/Root/_001001/combined_solid_green_2", prim_types=['Xform'])
        with green: 
            rep.modify.visibility(rep.distribution.choice([True, False]))
            # rep.modify.semantics([("class", "green")], mode="replace") 
        return green.node
     
     
    rep.randomizer.register(randomizeSun) 
    rep.randomizer.register(randomizeRedLight)
    rep.randomizer.register(randomizeYellowLight)
    rep.randomizer.register(randomizeGreenLight)

    carb.settings.get_settings().set("/omni/replicator/RTSubframes", 8)

    writer = rep.WriterRegistry.get("BasicWriter")
    writer.initialize(output_dir="_output", rgb=True, bounding_box_2d_tight=True)
    writer.attach([render_product])

    bbox = rep.AnnotatorRegistry.get_annotator("bounding_box_2d_tight") 
    bbox.attach(render_product)
                
    with rep.trigger.on_frame(max_execs=700, rt_subframes=12): 
        with camera:
            rep.modify.pose(position=rep.distribution.uniform((3.0, -6.0, 0.1), (7.5,  6.0, 0.8)), look_at=rep.distribution.uniform((-0.2, -0.3, 0.2), (0.2, 0.3, 0.6)))

        with map:
            rep.modify.pose(position=(0.075, 0.5, -0.59), rotation=rep.distribution.uniform((0, 0, -180), (0, 0, 180))) 

        rep.randomizer.randomizeSun()
        rep.randomizer.randomizeRedLight() 
        rep.randomizer.randomizeYellowLight()
        rep.randomizer.randomizeGreenLight()
 
    print("Script Ran!")


