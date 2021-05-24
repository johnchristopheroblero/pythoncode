class Bicycle:
    def __init__(self, factory):
self.tires = factory().add_tires()
self.frame = factory().add_frame()

classGenericFactory:
defadd_tires(self):
returnGenericTires()
defadd_frame(self):
returnGenericFrame()

classMountainFactory:
defadd_tires(self):
returnRuggedTires()
defadd_frame(self):
returnSturdyFrame()

classRoadFactory:
defadd_tires(self):
returnRoadTires()
defadd_frame(self):
returnLightFrame()

classGenericTires:
defpart_type(self):
return 'generic_tires'

classRuggedTires:
defpart_type(self):
return 'rugged_tires'

classRoadTires:
defpart_type(self):
return 'road_tires'

classGenericFrame:
defpart_type(self):
return 'generic_frame'

classSturdyFrame:
defpart_type(self):
return 'sturdy_frame'

classLightFrame:
defpart_type(self):
return 'light_frame'

bike = Bicycle(GenericFactory)
print(bike.tires.part_type())

print(bike.frame.part_type())

mountain_bike = Bicycle(MountainFactory)

print(mountain_bike.tires.part_type())

print(mountain_bike.frame.part_type())

road_bike = Bicycle(RoadFactory)

print(road_bike.tires.part_type())

print(road_bike.frame.part_type())
