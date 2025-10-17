local Aurora, namespace = ...

if namespace == nil and Aurora and Aurora.Aurora then
  namespace = Aurora
  Aurora = namespace.Aurora
elseif Aurora == nil and namespace and namespace.Aurora then
  Aurora = namespace.Aurora
end

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
