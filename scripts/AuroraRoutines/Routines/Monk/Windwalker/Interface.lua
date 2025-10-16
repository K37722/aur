local Aurora, namespace = ...

namespace.settings = namespace.settings or {
  cooldowns = true,
  defensives = true,
  aoe = true,
}

function namespace:GetSetting(name)
  if namespace.settings == nil then
    return nil
  end
  return namespace.settings[name]
end

return namespace.settings
