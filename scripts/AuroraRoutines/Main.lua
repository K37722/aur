local Aurora, namespace, Environment = ...

namespace = namespace or {}
namespace.name = namespace.name or "WindwalkerRetail"
namespace.class = "MONK"
namespace.spec = 3
namespace.Aurora = Aurora
namespace.Environment = Environment
namespace.config = namespace.config or {
  use_cooldowns = true,
  use_defensives = true,
  aoe_threshold = 3,
}

function namespace:GetSpellbook()
  local spellbooks = Aurora.SpellHandler.Spellbooks
  local classBook = spellbooks and spellbooks.monk and spellbooks.monk["3"]
  return classBook and classBook[self.name]
end

return namespace
