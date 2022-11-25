#include "ldmx.hpp"
#include <luainterface.hpp>
#include <pragma/pragma_module.hpp>

extern "C"
{
	void PRAGMA_EXPORT pragma_initialize_lua(Lua::Interface &l)
	{
		Lua::dmx::register_lua_library(l);
	}
};
