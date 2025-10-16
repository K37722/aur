local Aurora, namespace = ...

local UnitManager = Aurora.UnitManager
local enemies = Aurora.activeenemies

local function has_valid_target(target)
  return target and target.exists and not target.dead and target.enemy
end

local function enemy_count_around(unit)
  if not enemies or not enemies.around then
    return 0
  end
  return select(1, enemies:around(unit, 8)) or 0
end

local function ensure_spellbook()
  if namespace.spells then
    return true
  end
  local book = namespace:GetSpellbook()
  if not book then
    return false
  end
  namespace.spells = book.spells
  namespace.auras = book.auras
  namespace.talents = book.talents
  return namespace.spells ~= nil
end

local function use_defensives(player)
  if not namespace:GetSetting("defensives") then
    return false
  end
  local spells = namespace.spells
  if not spells then
    return false
  end
  if spells.ExpelHarm and player.hp and player.hp <= 65 then
    if spells.ExpelHarm:cast(player) then
      return true
    end
  end
  return false
end

local function use_cooldowns(player, target)
  if not namespace:GetSetting("cooldowns") then
    return false
  end
  local spells = namespace.spells
  if not spells then
    return false
  end
  local auras = namespace.auras or {}
  if spells.TouchOfDeath and target.hp and target.hp <= 15 then
    if spells.TouchOfDeath:cast(target) then
      return true
    end
  end
  if spells.StormEarthAndFire and not player:aura(auras.StormEarthAndFire) then
    if spells.StormEarthAndFire:cast(player) then
      return true
    end
  end
  if spells.Serenity and not player:aura(auras.Serenity) then
    if spells.Serenity:cast(player) then
      return true
    end
  end
  if spells.InvokeXuen then
    if spells.InvokeXuen:cast(target) then
      return true
    end
  end
  return false
end

local function aoe_priority(player, target, count)
  local spells = namespace.spells
  local threshold = namespace.config and namespace.config.aoe_threshold or 3
  if count < threshold then
    return false
  end
  if spells.FistsOfFury and not player.channeling then
    if spells.FistsOfFury:cast(player) then
      return true
    end
  end
  if spells.SpinningCraneKick then
    if spells.SpinningCraneKick:cast(player) then
      return true
    end
  end
  return false
end

local function single_target(player, target)
  local spells = namespace.spells
  if spells.StrikeOfTheWindlord and spells.StrikeOfTheWindlord:cast(target) then
    return true
  end
  if spells.WhirlingDragonPunch then
    local fof_cd = spells.FistsOfFury and spells.FistsOfFury:getcd() or 0
    local rsk_cd = spells.RisingSunKick and spells.RisingSunKick:getcd() or 0
    if fof_cd > 0 and rsk_cd > 0 then
      if spells.WhirlingDragonPunch:cast(player) then
        return true
      end
    end
  end
  if spells.FistsOfFury and not player.channeling then
    if spells.FistsOfFury:cast(player) then
      return true
    end
  end
  if spells.RisingSunKick then
    if spells.RisingSunKick:cast(target) then
      return true
    end
  end
  if spells.BlackoutKick then
    if spells.BlackoutKick:cast(target) then
      return true
    end
  end
  if spells.TigerPalm then
    if spells.TigerPalm:cast(target) then
      return true
    end
  end
  if spells.AutoAttack then
    spells.AutoAttack:cast(target)
  end
  return false
end

local function dps(player, target)
  if not ensure_spellbook() then
    return false
  end
  local count = enemy_count_around(target.exists and target or player)
  if count == 0 and target.exists then
    count = 1
  end
  if namespace:GetSetting("aoe") and aoe_priority(player, target, count) then
    return true
  end
  if single_target(player, target) then
    return true
  end
  return false
end

local function rotation()
  if not ensure_spellbook() then
    return
  end
  local player = UnitManager:Get("player")
  if not player or player.dead then
    return
  end
  if player:aura("Food") or player:aura("Drink") then
    return
  end
  if use_defensives(player) then
    return
  end
  local target = UnitManager:Get("target")
  if not has_valid_target(target) then
    return
  end
  if namespace.spells and namespace.spells.AutoAttack then
    namespace.spells.AutoAttack:cast(target)
  end
  if use_cooldowns(player, target) then
    return
  end
  if dps(player, target) then
    return
  end
end

Aurora:RegisterRoutine(rotation, namespace.class, namespace.spec, namespace.name)
