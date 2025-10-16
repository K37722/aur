local Aurora, namespace = ...

local NewSpell = Aurora.SpellHandler.NewSpell

local spells = {
  AutoAttack = NewSpell(6603),
  TigerPalm = NewSpell(100780, { ignoreMoving = true }),
  BlackoutKick = NewSpell(100784, { ignoreMoving = true }),
  RisingSunKick = NewSpell(107428, { ignoreMoving = true }),
  FistsOfFury = NewSpell(113656, { ignoreMoving = true }),
  WhirlingDragonPunch = NewSpell(152175, { ignoreMoving = true }),
  StrikeOfTheWindlord = NewSpell(392983, { ignoreMoving = true }),
  SpinningCraneKick = NewSpell(101546, { ignoreMoving = true }),
  StormEarthAndFire = NewSpell(137639, { ignoreMoving = true }),
  Serenity = NewSpell(152173, { ignoreMoving = true }),
  InvokeXuen = NewSpell(123904, { ignoreMoving = true }),
  TouchOfDeath = NewSpell(322109, { ignoreMoving = true }),
  ExpelHarm = NewSpell(115072, { ignoreMoving = true }),
  SpearHandStrike = NewSpell(116705, { ignoreMoving = true }),
  Paralysis = NewSpell(115078, { ignoreMoving = true }),
}

local auras = {
  StormEarthAndFire = 137639,
  Serenity = 152173,
  DanceOfChiJi = 325202,
  TeachingsOfTheMonastery = 202090,
  HitCombo = 196741,
}

local talents = {
  WhirlingDragonPunch = 152175,
  Serenity = 152173,
  StrikeOfTheWindlord = 392983,
}

Aurora.SpellHandler.PopulateSpellbook({
  spells = spells,
  auras = auras,
  talents = talents,
}, namespace.class, namespace.spec, namespace.name)

local book = namespace:GetSpellbook()
if book then
  namespace.spells = book.spells
  namespace.auras = book.auras
  namespace.talents = book.talents
end

return namespace.spells
