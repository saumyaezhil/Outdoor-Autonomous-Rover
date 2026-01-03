cmake_minimum_required(VERSION 3.8)
project(m2020_nav_description)

find_package(ament_cmake REQUIRED)

install(
  DIRECTORY urdf
  DESTINATION share/${PROJECT_NAME}
)

install(
  DIRECTORY meshes
  DESTINATION share/${PROJECT_NAME}
  
)
install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)


ament_package()
