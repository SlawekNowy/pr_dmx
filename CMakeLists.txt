cmake_minimum_required(VERSION 3.12)

include("./CMakeShared.txt")

set(PROJ_NAME pr_dmx)

project(${PROJ_NAME} CXX)

link_external_library(util_dmx)

add_external_library(lua)
add_external_library(luabind)

link_external_library(vfilesystem)
link_external_library(luasystem)
link_external_library(luabind)
link_external_library(sharedutils)
link_external_library(mathutil)
link_external_library(shared)
link_external_library(ishared)

add_include_dir(glm)
add_include_dir(luajit)

set(DEPENDENCY_UTIL_DMX_INCLUDE ${CMAKE_CURRENT_LIST_DIR}/external_libs/util_dmx/include CACHE PATH "" FORCE)
search_lib_recursive(DEPENDENCY_UTIL_DMX_LIBRARY external_libs/util_dmx/${BINARY_PRAGMA_DIR} util_dmx STATIC)

if (NOT TARGET util_dmx)
	add_subdirectory(external_libs/util_dmx)
endif()

# link_generic_module_libraries()
register_pragma_module(${PROJ_NAME})

add_dependencies(${PROJ_NAME} util_dmx)
