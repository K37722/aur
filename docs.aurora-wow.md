getting started
https://docs.aurora-wow.wt
https://docs.aurora-wow.wtf/getting-started/spells
https://docs.aurora-wow.wtf/getting-started/registeringrotation
https://docs.aurora-wow.wtf/getting-started/callbacks

Unit Properties
https://docs.aurora-wow.wtf/unit-properties/Unit%20-%20Properties
https://docs.aurora-wow.wtf/unit-properties/Power%20Types
https://docs.aurora-wow.wtf/unit-properties/Unit%20Methods
https://docs.aurora-wow.wtf/unit-properties/Aura%20Properties
https://docs.aurora-wow.wtf/unit-properties/Aura%20Methods
https://docs.aurora-wow.wtf/unit-properties/AuraTracking
https://docs.aurora-wow.wtf/unit-properties/Hidden%20Auras

Lists and Units
https://docs.aurora-wow.wtf/lists-and-units/Lists
https://docs.aurora-wow.wtf/lists-and-units/VirtualUnits

Spell
https://docs.aurora-wow.wtf/spell/overview
https://docs.aurora-wow.wtf/spell/
https://docs.aurora-wow.wtf/spell/payload
https://docs.aurora-wow.wtf/spell/methods

Missiles
https://docs.aurora-wow.wtf/missiles/overview
https://docs.aurora-wow.wtf/missiles/properties

Miscellaneous
https://docs.aurora-wow.wtf/misc/Draw
https://docs.aurora-wow.wtf/misc/Macro

https://docs.aurora-wow.wtf/misc/CombatLogReader
https://docs.aurora-wow.wtf/misc/Toast

StatusFrame
https://docs.aurora-wow.wtf/category/statusframe
https://docs.aurora-wow.wtf/status-frame/basic-usage

https://docs.aurora-wow.wtf/category/alert-system
https://docs.aurora-wow.wtf/alert/Alert%20Basics

https://docs.aurora-wow.wtf/category/utility-functions
https://docs.aurora-wow.wtf/functions/Utility%20Functions
https://docs.aurora-wow.wtf/functions/Frame

https://docs.aurora-wow.wtf/interface/overview
https://docs.aurora-wow.wtf/interface/ui-elements
https://docs.aurora-wow.wtf/interface/config-integration
https://docs.aurora-wow.wtf/interface/config-system

https://docs.aurora-wow.wtf/category/enums
https://docs.aurora-wow.wtf/enums/
https://docs.aurora-wow.wtf/enums/Lists

https://docs.aurora-wow.wtf/category/hooks
https://docs.aurora-wow.wtf/hooks/bigwigs
https://docs.aurora-wow.wtf/hooks/keyboard
https://docs.aurora-wow.wtf/hooks/encounter-manager
https://docs.aurora-wow.wtf/hooks/discord-webhook
https://docs.aurora-wow.wtf/hooks/state-registrar




Getting Started
Learn how to set up and create your first Aurora Framework project

📄️ Project Setup
This guide will help you set up your first Aurora Framework project.

📄️ Getting Started with Spells
Getting started with the spell system

📄️ Registering Your Rotation
Learn how to register and structure your rotation

📄️ Spell Callbacks
Learn how to use spell callbacks for advanced spell control

--
Project Setup
This guide will help you set up your first Aurora Framework project.

Namespace Setup
Why Use Your Own Namespace?
A namespace helps you:

Avoid conflicts with other routines
Share data between your files
Keep your code organized and modular
Prevent variable collisions
How to Pass Your Namespace
When loading your routines, Aurora passes three arguments to each file:

YourNamespace = {}

Your namespace is passed automatically when your routines are loaded. Simply use it in your files:

File Structure
Your project should follow this structure:

📂 scripts/
└── 📂 AuroraRoutines/      # Your routines
    ├── 📄 loadorder.json   # Load order configuration
    ├── 📄 Main.lua        # Core routine
    └── 📂 Routines/
        └── 📂 Warrior/
            └── 📂  Specialisation/ 
                ├── 📄 Spellbook.lua # Spellbook
                ├── 📄 Interface.lua # Interface
                └── 📄 Rotation.lua # Rotation

Initial Setup
Create the required directories:
mkdir -p scripts/AuroraRoutines

Create a loadorder.json file in your AuroraRoutines directory:
[
    "Main",
    "Routines/Warrior/Specialisation/Spellbook",
    "Routines/Warrior/Specialisation/Interface",
    "Routines/Warrior/Specialisation/Rotation"
]

File Extensions
Do not add .lua to the file paths in loadorder.json. The framework automatically adds the extension when loading the files.

Loading System
Aurora uses a dynamic loading system that:

Checks for the existence of your routines directory
Reads the loadorder.json file
Loads each file in the specified order
Best Practices
File Organization
Keep related functionality in separate files
Use descriptive file names
Maintain a logical load order
Place shared utilities in the Core file
Common Mistakes
Don't forget to update loadorder.json when adding new files
Ensure file names match exactly with the load order
Handle dependencies properly in your load order
Next Steps
Set up your development environment
Create your basic file structure
Implement your core functionality
Add your rotation logic
Test and refine
For more detailed information about specific components, check out:

Unit Properties
Virtual Units
Macro System

--
Getting Started with Spells
Registering Your Spellbook
After setting up your project, you'll need to register your spells with Aurora's spell system. This creates a centralized spellbook for your class that can be easily accessed throughout your code.

-- Create your spells
local NewSpell = Aurora.SpellHandler.NewSpell
Aurora.SpellHandler.PopulateSpellbook({
    spells = {
        AutoAttack = NewSpell(6603),
        Charge = NewSpell(100),
        ShieldSlam = NewSpell(23922),
        Ravager = NewSpell(228920, { radius = 8,}),
    },
    auras = {
        --Add Auras here
    },
    talents = {
        --Add Talents here
    },
}, "WARRIOR",3,"YourNamespace")

The 3 represents the Spec ID, and the "YourNamespace" is the name of your Project.

tip
See the Spell Overview for detailed information about creating and configuring spells.

Accessing Your Spells
Once registered, you can access your spells from anywhere in your code:

local spells = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.spells
local auras = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.auras
local talents = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.talents


If you would Play a Discipline Priest, you would use the following code:

local spells = Aurora.SpellHandler.Spellbooks.priest["1"].YourNamespace.spells
local auras = Aurora.SpellHandler.Spellbooks.priest["1"].YourNamespace.auras
local talents = Aurora.SpellHandler.Spellbooks.priest["1"].YourNamespace.talents


Best Practices
Keep Spellbook in Separate File Create a dedicated file (e.g., Spellbook.lua) for your spell definitions:
Next Steps
Once you have your spellbook set up, you can:

Learn about spell configuration options
Explore available spell methods
Implement your rotation logic using the registered spells

--
Registering Your Rotation
After setting up your spellbook and callbacks, you'll need to register your rotation with Aurora. This tells the framework what functions to call during combat.

Basic Structure

-- Get commonly used units
local target = Aurora.UnitManager:Get("target")
local player = Aurora.UnitManager:Get("player")

-- Get your spellbook
local spells = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.spells
local auras = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.auras
local talents = Aurora.SpellHandler.Spellbooks.warrior["3"].YourNamespace.talents

-- Define your combat rotation
local function Dps()
    if spells.ShieldBlock:execute() then return true end
    if spells.Ravager:execute() then return true end
    if spells.AutoAttack:execute() then return true end
    if spells.ShieldCharge:execute() then return true end
    if spells.ShieldSlam:execute() then return true end
    if spells.ThunderClap:execute() then return true end
    if spells.Execute:execute() then return true end
    if spells.Revenge:execute() then return true end
    if spells.HeroicThrow:execute() then return true end
    return false
end

-- Define out of combat actions
local function Ooc()
    -- Add your out of combat logic here
end

-- Register the rotation
Aurora:RegisterRoutine(function()
    -- Skip if player is dead or eating/drinking
    if player.dead or player.aura("Food") or player.aura("Drink") then return end

    -- Run appropriate function based on combat state
    if player.combat then
        Dps()
    else
        Ooc()
    end
end, "WARRIOR", 3, "YourNamespace")


Parameters Explained
The RegisterRoutine function takes these parameters:

Function - Your rotation logic
Class - Your class in uppercase (e.g., "WARRIOR", "PRIEST")
Spec - The specialization ID (e.g., 3 for Protection)
Namespace - Your project's namespace
Best Practices
Organization
Keep your rotation logic clean and organized
Use separate functions for different aspects (DPS, healing, utility)
Check important conditions first (dead, eating/drinking)
Return true when an action is taken
Common Patterns
Basic Combat Check
if player.combat then
    Dps()
else
    Ooc()
end

Skip Conditions
if player.dead or player.aura("Food") or player.aura("Drink") then return end


Action Priority
local function Dps()
    -- Defensive cooldowns first
    if spells.ShieldBlock:execute() then return true end
    
    -- Then major cooldowns
    if spells.Ravager:execute() then return true end
    
    -- Then regular rotation
    if spells.ShieldSlam:execute() then return true end
    if spells.ThunderClap:execute() then return true end
    
    return false
end

Next Steps
Learn about Callbacks for spell-specific logic
Explore Unit Properties for more conditions
Study Spell Methods for all available spell actions

--
Spell Callbacks
Spell callbacks provide a powerful way to define custom logic for when and how spells should be cast. Instead of checking conditions in your rotation, you can attach the logic directly to the spell.

Basic Structure
spells.SpellName:callback(function(spell, logic)
    -- Your spell logic here
    if condition then
        spell:cast(target)
    end
end)

Example Callbacks
Healing Spell with Health Threshold
spells.ImpendingVictory:callback(function(spell, logic)
    local healAmount = player.healthmax * 0.2              -- Calculate 20% of max health
    local healthMissing = player.healthmax - player.health -- Calculate missing health

    if healthMissing >= healAmount * 0.8 then              -- Use if we're missing at least 80% of the heal amount
        spell:cast(player)
    end
end)


Basic Target Spell
spells.ShieldSlam:callback(function(spell, logic)
    spell:cast(target)
end)

AOE Spell with Enemy Count
spells.ThunderClap:callback(function(spell, logic)
    if player.enemiesaround(8) > 0 then
        spell:cast(player)
    end
end)

Distance and AOE Check
spells.ShieldCharge:callback(function(spell, logic)
    if target.enemiesaround(8) > 0 and target.distanceto(player) <= 10 then
        spell:cast(target)
    end
end)


Arc Check for Cleave Spells
spells.Revenge:callback(function(spell, logic)
    Aurora.activeenemies:each(function(enemy)
        if enemy.inarcof(player, 8, 180) then
            spell:cast(player)
        end
    end)
end)

Execute Phase Spell
spells.Execute:callback(function(spell, logic)
    Aurora.activeenemies:each(function(enemy)
        if enemy.hp <= 20 then
            spell:cast(enemy)
        end
    end)
end)

Common Patterns
Health-Based Decisions
spell:callback(function(spell, logic)
    if player.hp < 40 then
        spell:cast(player)
    end
end)

Resource-Based Decisions
spell:callback(function(spell, logic)
    if player.rage >= 40 then
        spell:cast(target)
    end
end)

Enemy Count Checks
spell:callback(function(spell, logic)
    if player.enemiesaround(8) >= 3 then
        spell:cast(player)
    end
end)

Next Steps
Learn about Unit Properties for more targeting options
Explore Object Manager for advanced unit handling
Study Spell Methods for all available spell actions

--
Unit Properties
Documentation for Unit properties, methods, and related functionality including aura handling.

📄️ Unit Properties
This document outlines all available properties for the Unit class in the Aurora Framework.

📄️ Power Types
This document outlines all available power types and their properties in the Aurora Framework.

📄️ Unit Methods
This document outlines all available methods for the Unit class in the Aurora Framework.

📄️ Aura Properties
This outlines all available properties for Auras in Aurora.

📄️ Aura Methods
This outlines all available methods for working with Auras in Aurora.

📄️ Aura Tracking
This outlines how to use the Aura Tracking system to monitor auras across multiple units.

📄️ Hidden Auras
What are Hidden Auras?

--
Unit Properties
This document outlines all available properties for the Unit class in the Aurora Framework.

Properties
Identification
guid
guid: string

The unique identifier for the unit

unit
unit: string|userdata

WoW unit token or object

id
id: boolean|number

Unit's ID

name
name: string

Unit's name

pointer
pointer: userdata|nil

Unit's memory pointer

creator
creator: guid|nil

Unit's creator

effects
effects: array

Returns a array of current active spell effects and there visual id and location

Health & Status
health
health: number

Current health value

healthmax
healthmax: number

Maximum health value

healthpercent
healthpercent: number

Health percentage (0-100)

hp
hp: number

Alias for health

effectivehp
effectivehp: number;

Effective health points (Taking absorbs and incoming heals into account)

healabsorb
healabsorb: number

Returns the total amount of healing absorption on the unit

stagger
stagger: number

Returns the stagger value of the unit

staggerpct
staggerpct: number

Returns the stagger percentage of the unit from 0 to 100

staggerhealth
staggerhealth: number

Returns the incoming stagger damage of the unit

dead
dead: boolean

Whether the unit is dead

alive
alive: boolean

Whether the unit is alive

exists
exists: boolean

Whether the unit exists

Combat & Threat
combat
combat: boolean

Whether the unit is in combat

threat
threat: number

Unit's threat level

aggro
aggro: boolean

Whether the unit has aggro

aggressive
aggressive: boolean

Whether the unit is aggressive

enemy
enemy: boolean

Whether the unit is an enemy

friend
friend: boolean

Whether the unit is friendly

reaction
reaction: number

Unit's reaction level towards the player

Movement & Position
position
position: Position

Unit's position in 3D space

speed
speed: number

Unit's movement speed

moving
moving: boolean

Whether the unit is moving

movingatall
movingatall: boolean

Whether the unit is moving at all

invehicle
invehicle: boolean

Whether the unit is in a vehicle

standing
standing: boolean

Whether the unit is standing still

height
height: number

Unit's height

combatreach
combatreach: number

Unit's combat reach distance

rotation
rotation: number

Unit's rotation in radians

reach
reach: number

Alias for combatreach

mounted
mounted: boolean

Whether the unit is mounted

timemoving
timemoving: number

Time in seconds the unit has been continuously moving

timestanding
timestanding: number

Time in seconds the unit has been continuously standing still

timecombat
timecombat: number

Time in seconds the unit has been continuously in combat

position
position: Position

Unit's position in 3D space

timeaggro
timeaggro: number

Time in seconds the unit has been aggroed

Unit Type & Classification
class
class: string

Unit's class name (localized)

class2
class2: string

Unit's class name in English

classid
classid: number

Unit's class ID

spec
spec: number

Unit's specialization ID

race
race: string

Unit's race name (localized)

race2
race2: string

Unit's race name in English

level
level: number

Unit's level

type
type: number

Unit's type ID

typestring
typestring: string

Unit's type as string

Unit Type Checks
isboss
isboss: boolean

Whether the unit is a boss

ishumanoid
ishumanoid: boolean

Whether the unit is a humanoid

isbeast
isbeast: boolean

Whether the unit is a beast

isundead
isundead: boolean

Whether the unit is undead

isdemon
isdemon: boolean

Whether the unit is a demon

isdragonkin
isdragonkin: boolean

Whether the unit is a dragonkin

iselemenetal
iselemenetal: boolean

Whether the unit is an elemental

isgiant
isgiant: boolean

Whether the unit is a giant

ismechanical
ismechanical: boolean

Whether the unit is mechanical

istotem
istotem: boolean

Whether the unit is a totem

isaberration
isaberration: boolean

Whether the unit is an aberration

isuncategorized
isuncategorized: boolean

Whether the unit is uncategorized

Player-Facing Properties
facing
facing: number

Unit's facing direction in radians

playerfacing
playerfacing: boolean

Whether the player is facing the unit within 90 degrees

playerfacing30
playerfacing30: boolean

Whether the player is facing the unit within 30 degrees

playerfacing45
playerfacing45: boolean

Whether the player is facing the unit within 45 degrees

playerfacing60
playerfacing60: boolean

Whether the player is facing the unit within 60 degrees

playerfacing90
playerfacing90: boolean

Whether the player is facing the unit within 90 degrees

playerfacing180
playerfacing180: boolean

Whether the player is facing the unit within 180 degrees

Unit Counting
enenmiesaround(radius)
enenmiesaround(radius: number): number

Returns the number of enemy units within the specified radius of this unit

friendsaround(radius)
friendsaround(radius: number): number

Returns the number of friendly units within the specified radius of this unit

-- Example: Count friends within 10 yards
local nearbyFriends = unit.friendsaround(10)

friendsaroundhp(distance, hp)
friendsaroundhp(distance: number, hp: number): number

Returns the number of friendly units within the specified distance that are below the specified health percentage

-- Example: Count friends within 20 yards below 50% health
local injuredFriends = player.friendsaroundhp(20, 50)

Group Status
party
party: boolean

Whether the unit is in party

group
group: boolean

Whether the unit is in group

raid
raid: boolean

Whether the unit is in raid

ininstance
ininstance: boolean

Whether the unit is in an instance

inraid
inraid: boolean

Whether the unit is in a raid

Role Properties
role
role: string

Returns the unit's assigned role in group ("TANK", "HEALER", "DAMAGER", or "None")

ishealer
ishealer: boolean

Whether the unit is assigned as a healer

isdps
isdps: boolean

Whether the unit is assigned as a damage dealer

istank
istank: boolean

Whether the unit is assigned as a tank

Visibility & Interaction
visible
visible: boolean

Whether the unit is visible

los
los: boolean

Whether the unit is in line of sight

lootable
lootable: boolean

Whether the unit is lootable

skinnable
skinnable: boolean

Whether the unit is skinnable

tapdenied
tapdenied: boolean

Whether tap is denied for the unit

charmed
charmed: boolean

Whether the unit is charmed

Casting Information
casting
casting: string|false

Current cast name or false

casting1
casting1: string|false

Cast text

casting2
casting2: string|false

Cast texture

castingstart
castingstart: number

Cast start time

castingend
castingend: number

Cast end time

castingtrade
castingtrade: boolean

Whether casting a trade spell

castingid
castingid: number

ID of the spell being cast

castingnotinterruptible
castingnotinterruptible: boolean

Whether the cast cannot be interrupted

castinginterruptible
castinginterruptible: boolean

Whether the cast can be interrupted

castingspellid
castingspellid: number

ID of the spell being cast

castingremains
castingremains: number

Time remaining on the cast

castingpct
castingpct: number

Percentage of cast completed

channeling
channeling: string|false

Current channel name or false

channeling1
channeling1: string|false

Channel text

channeling2
channeling2: string|false

Channel texture

channelingstart
channelingstart: number

Channel start time in seconds

channelingend
channelingend: number

Channel end time in seconds

channelingid
channelingid: number

ID of the channeled spell

channelingnotinterruptible
channelingnotinterruptible: boolean

Whether the channel cannot be interrupted

channelinginterruptible
channelinginterruptible: boolean

Whether the channel can be interrupted

channelingspellid
channelingspellid: number

Spell ID of the channeled spell

channelingremains
channelingremains: number

Percentage of channel time remaining (100 to 0)

channelingpct
channelingpct: number

Percentage of channel completed (100 to 0)

Combat Statistics
ttd
ttd: number

Time to die prediction

Power Types
Power types and their properties are documented in detail in the Power Types section.

Methods
Unit methods are documented in detail in the Unit Methods section.

Usage Example
-- All property accesses are actually method calls through metatables
local target = Aurora.UnitManager:Get("target")
local player = Aurora.UnitManager:Get("player")

-- Basic target checks
if target.exists and target.enemy and target.alive then
    if target.hp < 20 and target.distanceto(player) < 30 then
        -- Execute logic here
    end
end

-- Example showing type checks and positioning
if target.ishumanoid and not target.ismechanical then
    if target.playerfacing  then
        -- Use frontal cone melee ability on humanoid target
    end
end

-- Aura examples
if target.exists then
    -- Check for a specific debuff
    local hasDeBuff = target.aura(12345)
    if hasDeBuff then
        local remaining = target.auraremains(12345)
        if remaining < 3 then
            -- Refresh debuff before it expires
        end
    end
    
    -- Check aura stacks
    local stacks = target.auracount(67890)
    if stacks >= 5 then
        -- Use ability that consumes stacks
    end
    
    -- Check for any aura from a list
    local auraList = {12345, 67890, 11223}
    if target.aurafrom(auraList) then
        -- Unit has at least one of the auras
    end
end

-- Combat and casting checks
if target.exists and target.casting then
    if target.castinginterruptible and target.castingpct > 50 then
        if player.distanceto(target) < 30 then
            -- Interrupt the cast
        end
    end
end


Notes
note
Although properties appear to be accessed using dot notation (e.g., unit.health), they are actually method calls through Lua metatables
For clarity in documentation, we show them as properties, but internally they are methods
All "properties" can be called using either dot notation (unit.health) or method notation (unit:health())
The unit property can accept either a WoW unit token (e.g., "target", "player") or a unit object
Unit References
target
Returns a Unit object representing the unit's current target.

local unit = Aurora.UnitManager:Get("player")
local target = unit.target

if target.exists then
    print("My target is " .. target.name)
end

-- Chain targeting
if unit.target.target.exists then
    print("My target's target is " .. unit.target.target.name)
end


Unit Characteristics
These properties indicate whether a unit can be affected by various crowd control abilities. In dungeons (party instances), these are determined by the unit's type configuration. Outside of dungeons, all return true by default.

istauntable
istauntable: boolean

Whether the unit can be taunted. In dungeons, this is determined by the unit's taunt configuration.

isgrippable
isgrippable: boolean

Whether the unit can be gripped (Death Grip, etc.). In dungeons, this is determined by the unit's grip configuration.

isfearable
isfearable: boolean

Whether the unit can be feared. In dungeons, this is determined by the unit's fear configuration.

isrootable
isrootable: boolean

Whether the unit can be rooted. In dungeons, this is determined by the unit's root configuration.

issilenceable
issilenceable: boolean

Whether the unit can be silenced. In dungeons, this is determined by the unit's silence configuration.

isslowable
isslowable: boolean

Whether the unit can be slowed. In dungeons, this is determined by the unit's slow configuration.

isstunable
isstunable: boolean

Whether the unit can be stunned. In dungeons, this is determined by the unit's stun configuration.

isincapacitable
isincapacitable: boolean

Whether the unit can be incapacitated. In dungeons, this is determined by the unit's incapacitate configuration.

note
All these characteristics return true by default outside of dungeons. Inside dungeons, they check the unit's specific configuration in Aurora.Enums.UnitEnums.

-- Example: Check if a unit can be controlled before using CC
local target = Aurora.UnitManager:Get("target")

if target.exists and target.enemy then
    if target.isstunable then
        -- Use stun ability
    elseif target.isrootable then
        -- Use root ability instead
    elseif target.isslowable then
        -- Fall back to slow effect
    end
end

--
Power Types
This document outlines all available power types and their properties in the Aurora Framework.

Overview
Power types represent different resources used by classes in World of Warcraft. Each power type has a set of properties that can be accessed through the Unit class.

Available Power Types
Power Type	ID	Description	Classes
Mana	0	Primary resource for casters	Priest, Mage, Warlock, Druid, Shaman, Monk, Paladin
Rage	1	Generated by taking/dealing damage	Warrior, Druid (Bear)
Focus	2	Hunter's primary resource	Hunter
Energy	3	Fast-regenerating resource	Rogue, Druid (Cat), Monk
Combo Points	4	Secondary resource for finishers	Rogue, Druid (Cat)
Runes	5	Death Knight's primary resource	Death Knight
Runic Power	6	Generated by rune spending	Death Knight
Soul Shards	7	Generated by specific abilities	Warlock
Astral Power	8	Generated by spells and abilities	Druid (Balance)
Holy Power	9	Generated by specific abilities	Paladin
Alternate Power	10	Encounter-specific resource	Any
Maelstrom	11	Generated by specific abilities	Shaman
Chi	12	Generated by abilities	Monk
Insanity	13	Generated by spells	Priest (Shadow)
Arcane Charges	16	Generated by specific spells	Mage (Arcane)
Fury	17	Generated by abilities	Demon Hunter
Pain	18	Tank resource	Demon Hunter (Vengeance)
Essence	19	Primary resource	Evoker
Properties
Each power type has the following properties available:

Basic Properties
unit.<type>         -- Current power value
unit.<type>max      -- Maximum power value
unit.<type>pct      -- Power percentage (0-100)
unit.<type>deficit  -- Amount of power missing from maximum

Regeneration Properties
unit.<type>regen    -- Power regeneration rate per second
unit.<type>timeto(value)  -- Time in seconds until reaching specified value
unit.<type>timetomax      -- Time in seconds until reaching maximum power


Alternative Names
Some power types have alternative names for convenience:

Power Type	Alternative Names
Combo Points	cp, combopoints
Astral Power	ap, astralpower, lunarpower
Soul Shards	shards, soulshards
Usage Examples
Basic Power Checks
local player = Aurora.UnitManager:Get("player")

-- Basic power value check
if player.mana < 1000 then
    -- Low mana handling
end

-- Percentage check
if player.ragepct > 60 then
    -- Use rage dump ability
end

-- Maximum value check
if player.energy == player.energymax then
    -- Use energy to avoid capping
end

Resource Planning
-- Wait for resource regeneration
if player.energy < 50 and player.energytimeto(80) < 2 then
    -- Resource will reach 80 in less than 2 seconds
    return true
end

-- Check if resource is regenerating quickly
if player.energyregen > 10 then
    -- Fast energy regeneration period
end

-- Resource deficit check
if player.manadeficit > 10000 then
    -- Use mana regeneration cooldown
end

Secondary Resources
-- Combo point management
if player.combopoints >= 5 then
    -- Use finisher
elseif player.combopoints == 0 then
    -- Use builder
end

-- Holy power management
if player.holypower >= 3 then
    -- Use spender
end

Best Practices
Resource Management
Always check resource availability before casting abilities
Consider regeneration rates for resource planning
Use percentage checks for relative resource levels
Monitor resource deficits for regeneration abilities
Resource Caps
Be careful not to waste resources by:

Letting fast-regenerating resources cap (Energy, Focus)
Using generators at maximum secondary resources (Combo Points, Holy Power)
Ignoring resource regeneration mechanics
Notes
Power Type Access
All power properties are accessed through the unit object
Properties are case-sensitive
Use alternative names where they make code more readable

---

Unit Methods
This document outlines all available methods for the Unit class in the Aurora Framework.

Position & Movement Methods
behind(target)
behind(target: Unit) -> boolean

Check if unit is behind target

infront(target)
infront(target: Unit) -> boolean

Check if unit is in front of target

melee(target)
melee(target: Unit) -> boolean

Check if unit is in melee range of target

distanceto(target)
distanceto(target: Unit | {x: number, y: number, z: number}) -> number


Get distance to target. The target can be either:

A Unit object
A position table with x, y, z coordinates
Returns the distance in yards.

distancetoliteral(target)
distancetoliteral(target: Unit) -> number

Get literal distance to target (ignoring combat reach)

futureposition(timeframe)
futureposition(time: Number) -> Array: number

Combat Methods
inarcof(target, size , arc , rotation)
inarcof(target: Unit, size: number, arc: number, rotation: number) -> boolean


Check if unit is within a specific arc of target

enemiesaround(radius)
enemiesaround(radius: number) -> number

Count enemies within radius

haslos(target)
haslos(target: Unit  | {x: number, y: number, z: number}) -> boolean


Check line of sight to target

Unit Interaction Methods
settarget(target)
settarget(target: Unit|nil) -> boolean

Set unit's target

isunit(target)
isunit(target: Unit) -> boolean

Check if unit is the same as target

interact()
interact() -> boolean

Interact with the unit

Position & Movement
local target = Aurora.UnitManager:Get("target")
local player = Aurora.UnitManager:Get("player")

-- Check if player is behind target
if player.behind(target) then
    -- Use backstab ability
end

-- Check distance and line of sight
if target.distanceto(player) < 30 and target.haslos(player) then
    -- Cast ranged ability
end


Combat & Targeting
local player = Aurora.UnitManager:Get("player")

-- Count nearby enemies
local enemyCount = player.enemiesaround(8)
if enemyCount >= 3 then
    -- Use AoE ability
end

-- Set target and interact
local enemy = Aurora.UnitManager:Get("target")
if enemy.exists and player.settarget(enemy) then
    player.interact()
end

Best Practices
Method Usage
Always check unit existence before calling methods
Use appropriate range checks before attempting interactions
Consider line of sight for ranged abilities
Cache frequently accessed values for better performance
Common Pitfalls
Don't assume target existence
Check range before melee abilities
Verify line of sight for ranged abilities
Consider unit type restrictions for certain interactions
Notes
Method Calls
All methods can be called using either:

Colon syntax: unit:method(args)
Dot syntax with self: unit.method(unit, args)
Return Values
Most methods return false or nil on failure
Check return values for critical operations
Some methods may return multiple values

--
ura Properties
This outlines all available properties for Auras in Aurora.

Basic Properties
name
name: string

The name of the aura

icon
icon: string

The texture path for the aura's icon

count
count: number

Number of stacks/applications (0 if not stacked)

charges
charges: number

Current number of charges

maxCharges
maxCharges: number

Maximum number of charges possible

dispelType
dispelType: string

The type of dispel required (Magic, Curse, etc.)

duration
duration: number

Total duration of the aura in seconds

expirationTime
expirationTime: number

When the aura will expire (GetTime() + duration)

sourceUnitGuid
sourceUnitGuid: string

The GUID of the unit that applied the aura

spellId
spellId: number

The spell ID of the aura

startTime
startTime: number

When the aura was applied (GetTime())

State Properties
isStealable
isStealable: boolean

Whether the aura can be stolen by Mages

nameplateShowPersonal
nameplateShowPersonal: boolean

Whether to show on personal nameplate

nameplateShowAll
nameplateShowAll: boolean

Whether to show on all nameplates

canApplyAura
canApplyAura: boolean

Whether the aura can be applied

isBossAura
isBossAura: boolean

Whether it's a boss aura

isFromPlayerOrPlayerPet
isFromPlayerOrPlayerPet: boolean

Whether applied by player or their pet

isHarmful
isHarmful: boolean

Whether the aura is harmful (debuff)

isHelpful
isHelpful: boolean

Whether the aura is helpful (buff)

isNameplateOnly
isNameplateOnly: boolean

Whether the aura only shows on nameplates

isRaid
isRaid: boolean

Whether it's a raid aura

type
type: string

"HARMFUL" for debuffs or "HELPFUL" for buffs

Technical Properties
timeMod
timeMod: number

Time modification value

auraInstanceID
auraInstanceID: number

Unique instance ID for this aura application

points
points: table

Points data associated with the aura

Usage Example
local target = Aurora.UnitManager:Get("target")
local myDebuff = target.aura(12345)

if myDebuff then
    print("Aura name:", myDebuff.name)
    print("Charges:", myDebuff.charges)
    print("Duration:", myDebuff.duration)
    print("Is from player:", myDebuff.isFromPlayerOrPlayerPet)
    
    if myDebuff.isStealable then
        -- Can be stolen by Mage
    end
end


note
All properties are accessed through method calls internally, but can be used with dot notation for convenience.

--

Aura Methods
This outlines all available methods for working with Auras in Aurora.

Aura Collection Methods
allauras
allauras -> table

Get all auras on the unit

local target = Aurora.UnitManager:Get("target")
local allAuras = target.allauras
for _, aura in ipairs(allAuras) do
    print(aura.name, aura.remaining)
end

alldispelauras
alldispelauras -> table

Get all dispellable auras on the unit

local target = Aurora.UnitManager:Get("target")
local dispellableAuras = target.alldispelauras
for _, aura in ipairs(dispellableAuras) do
    if aura.dispellable then
        -- Handle dispellable aura
    end
end

Individual Aura Methods
aura(id, sourceObject)
aura(id: number|string, sourceObject: Unit|nil) -> Aura|nil

Get specific aura by ID

aurauptime(id, sourceObject)
aurauptime(id: number|string, sourceObject: Unit|nil) -> number


Get aura uptime

auraremains(id, sourceObject)
auraremains(id: number|string, sourceObject: Unit|nil) -> number


Get aura remaining time

auracount(id, sourceObject)
auracount(id: number|string, sourceObject: Unit|nil) -> number


Get aura stack count

aurafrom(array, sourceObject)
aurafrom(array: number[], sourceObject: Unit|nil) -> boolean


Check if unit has aura from array

Usage Examples
local target = Aurora.UnitManager:Get("target")

-- Check for specific aura
local myDebuff = target.aura(12345)
if myDebuff and myDebuff.remaining < 3 then
    -- Refresh debuff
end

-- Check for any aura from a list
local auraList = {12345, 67890, 11223}
if target.aurafrom(auraList) then
    -- Unit has at least one of the auras
end

-- Get all dispellable auras
local dispellableAuras = target.alldispelauras
for _, aura in ipairs(dispellableAuras) do
    print("Can dispel:", aura.name)
end

--
Aura Tracking
This outlines how to use the Aura Tracking system to monitor auras across multiple units.

TrackAuras
Aurora.TrackAuras(auraIds: string|number|string[]|number[], callback: function) -> function


Tracks specific auras across all units and calls your callback when those auras are added, updated, or removed.

Parameters:
auraIds - Single spell ID/name or an array of spell IDs/names to track
callback - Function called with parameters:
unit - The unit that has the aura
aura - The aura object with all properties
event - Event type ("ADD_OR_UPDATE" or "REMOVE")
Returns:
A function that when called will unregister the tracker
Basic Usage
-- Track a single aura by ID
local unregisterTracker = Aurora.TrackAuras(462854, function(unit, aura, event)
    if event == "ADD_OR_UPDATE" then
        print("Aura detected:", aura.name, "on", unit.name)
    elseif event == "REMOVE" then
        print("Aura removed:", aura.name, "from", unit.name)
    end
end)

-- Track multiple auras
local aurasToTrack = {
    462854,  -- First aura ID
    123456,  -- Second aura ID
    "Power Word: Shield" -- Aura by name
}

local unregisterTracker = Aurora.TrackAuras(aurasToTrack, function(unit, aura, event)
    -- Handler code
end)

-- When you want to stop tracking:
unregisterTracker()


Advanced Usage
-- Track important debuffs and count affected units
local debuffCount = 0
local affectedUnits = {}

local unregisterTracker = Aurora.TrackAuras({12345, 67890}, function(unit, aura, event)
    if event == "ADD_OR_UPDATE" and not affectedUnits[unit.guid] then
        affectedUnits[unit.guid] = true
        debuffCount = debuffCount + 1
        print("Units affected by tracked debuffs:", debuffCount)
    elseif event == "REMOVE" then
        affectedUnits[unit.guid] = nil
        debuffCount = debuffCount - 1
    end
end)


Event Types
The callback receives one of these event types:

ADD_OR_UPDATE - Called when an aura is first detected or when it updates
REMOVE - Called when an aura is removed from a unit

--

Hidden Auras
What are Hidden Auras?
Hidden auras are buffs and debuffs that are normally not visible to players through the standard UI. These include special effects like tier set bonuses, internal buff tracking, and other game mechanics that operate behind the scenes.

Aurora provides access to these hidden auras through the Aurora.hiddenauras table.

Accessing Hidden Auras
The Aurora.hiddenauras table contains all detected hidden auras on the player, indexed by spell ID.

-- Check if a specific hidden aura exists
local tierSetBonus = Aurora.hiddenauras[123456] -- replace with actual spell ID

if tierSetBonus then
    print("Tier set bonus is active with " .. tierSetBonus.stacks .. " stacks")
end

-- Iterate through all hidden auras
for spellId, auraInfo in pairs(Aurora.hiddenauras) do
    print(spellId .. ": " .. auraInfo.name)
end


Common Hidden Auras
Hidden auras typically include:

Tier set bonuses
Special encounter mechanics
Aura Properties
Each hidden aura entry contains the same properties as regular auras:

name: The name of the aura
icon: The icon texture of the aura
stacks: Number of stacks
duration: Total duration of the aura
spellId: The spell ID of the aura
And other standard aura properties
See Aura Properties for a complete list of available properties.

Usage Examples
Tracking Tier Set Bonuses
local function HasTierSetBonus(tier, setPieces)
    -- Example tier set aura IDs - replace with actual IDs 
    local tierBonusAuras = {
        [2] = 123456, -- 2-piece bonus aura
        [4] = 123457  -- 4-piece bonus aura
    }
    
    return Aurora.hiddenauras[tierBonusAuras[setPieces]] ~= nil
end

if HasTierSetBonus("T30", 4) then
    -- Player has 4-piece tier set bonus
    -- Adjust rotation accordingly
end
--
Lists
What are they?
Lists in Aurora Framework are powerful collections of Unit objects that provide various methods for filtering, iterating, and manipulating groups of units. Each list is automatically updated and managed by the ObjectManager.

Available Lists
enemies
Contains enemy units that are relevant to the current context.

local enemies = Aurora.enemies

friends
Contains friendly units, including those not in your group.

local friends = Aurora.friends

group
Contains group members (party/raid) excluding the player.

local group = Aurora.group

fgroup
Contains group members including the player (full group).

local fgroup = Aurora.fgroup

activeenemies
Contains enemy units that are in combat and have threat.

local activeenemies = Aurora.activeenemies

dead
Contains all dead units.

local dead = Aurora.dead

units
Contains all units regardless of type.

local units = Aurora.units

objects
Contains all game objects.

local objects = Aurora.objects

missiles
Contains all missiles.

local missiles = Aurora.missiles

areatriggers
Contains all areatriggers.

local areatriggers = Aurora.areatriggers

List Methods
each(callback)
Iterate through the list with a callback that receives the unit, index, and uptime. Returning true from the callback breaks the loop.

enemies:each(function(unit, i, uptime)
    print("Enemy #" .. i .. " has been visible for " .. uptime .. " seconds")
    if unit.hp < 20 then
        return true -- breaks the loop
    end
end)


filter(callback)
Create a new list containing units that match the callback criteria.

local lowHealth = enemies:filter(function(unit)
    return unit.hp < 50
end)

first(callback)
Get the first unit that matches the callback criteria.

local target = enemies:first(function(unit)
    return unit.hp < 20
end)

random()
Get a random unit from the list.

local randomEnemy = enemies:random()

print(randomEnemy.name)

sort(callback)
Sort the list based on the callback criteria.

enemies:sort(function(a, b)
    return a.hp < b.hp
end)

Usage Examples
Basic Iteration
-- Loop through enemies
enemies:each(function(enemy, index, uptime)
    print("Processing enemy #" .. index .. " visible for " .. uptime .. " seconds")
    if enemy.hp < 20 and enemy.distance < 30 then
        -- Do something with low health nearby enemy
        return true -- break the loop
    end
end)


Filtering and Chaining
-- Get low health enemies and loop through them
enemies:filter(function(unit)
    return unit.hp < 50
end):each(function(unit)
    -- Heal or damage low health units
end)

Complex Conditions
-- Find specific types of units
local targets = enemies:filter(function(unit)
    return unit.ishumanoid 
        and not unit.dead 
        and unit.distanceto(player) < 40
        and unit.los
end)

    targets:each(function(unit)
        -- Process filtered units
    end)

Group Management
-- Heal group members
group:each(function(member)
    if member.hp < 80 and member.distanceto(player) < 40 then
        -- Heal the group member
        return true
    end
end)


Best Practices
Performance
Use each instead of Lua's for loops for better control flow
Chain methods when possible to reduce iterations
Use filter when you need to reuse a filtered list multiple times
Break loops early when you find what you need
Common Pitfalls
Always check unit existence before accessing properties
Consider range and line of sight for actions
Notes
List Updates
Lists only contain valid units/objects
Method Returns
each: Returns nil. When the callback returns true, the loop breaks early
filter: Returns a new list with filtered units
first: Returns the first matching unit or none
random: Returns a random unit from the list

--
Virtual Units
Virtual Units provide a way to dynamically reference units based on roles or other criteria. They automatically resolve to the appropriate unit based on your current group composition and context.

Basic Usage
local tank = Aurora.UnitManager.tank
local healer = Aurora.UnitManager.healer

-- Use virtual units like normal units
if tank.exists then
    print("Tank is " .. tank.name)
end

Built-in Virtual Units
Tank
The tank virtual unit resolves in the following order:

Assigned Main Tank in raid
Player with Tank role in group
Player if they are a tank
Returns none unit if no tank is found
local tank = Aurora.UnitManager.tank

-- Examples
if tank.exists then
    if tank.hp < 50 then
        -- Heal the tank
    end
    
    if tank.distanceto(player) < 40 then
        -- Stay close to tank
    end
end

Healer
The healer virtual unit resolves in the following order:

Player with Healer role in group
Player if they are a healer
Returns none unit if no healer is found
local healer = Aurora.UnitManager.healer

if healer.exists and healer.manapct < 20 then
    -- Help conserve healer's mana
end

Target
The target property returns a virtual unit representing any unit's current target:

local myTarget = player.target
local tankTarget = tank.target
local healerTarget = healer.target

-- Chain targeting
local targetsTarget = player.target.target -- returns target's target as a unit


This allows you to:

Access all unit properties on the target
Chain target references (target of target)
Handle non-existent targets safely (returns none unit if no target)
Example usage:

local unit = Aurora.UnitManager:Get("player")

-- Check if target exists and is an enemy
if unit.target.exists and unit.target.enemy then
    -- Do something with the target
end

-- Check target's target
if unit.target.target.exists then
    print("My target is targeting " .. unit.target.target.name)
end

-- Check if tank's target matches your target
if tank.target.guid == player.target.guid then
    print("We're targeting the same unit!")
end


Custom Virtual Units
You can register your own virtual units:

-- Register a virtual unit for the lowest health party member
Aurora.UnitManager:RegisterVirtualUnit("lowestHealth", function(self)
    local lowest = nil
    local lowestHP = 100
    
    Aurora.fgroup:each(function(unit)
        if unit.alive and unit.hp < lowestHP then
            lowest = unit
            lowestHP = unit.hp
        end
        return false
    end)
    
    return lowest or self:Get("none")
end)

-- Use it like any other unit
local needsHealing = Aurora.UnitManager.lowestHealth
if needsHealing.exists and needsHealing.hp < 50 then
    -- Heal them
end


Best Practices
Usage
Virtual units are recalculated each time they're accessed
Use them when you need dynamic unit resolution
Cache the result if you need to use it multiple times in quick succession
Performance
Avoid accessing virtual units in tight loops
Don't create virtual units for static references
Remember that resolution order matters
Common Use Cases
Tank Swapping
local tank = Aurora.UnitManager.tank
local offtank = Aurora.UnitManager:RegisterVirtualUnit("offtank", function(self)
    if IsInRaid() then
        for i = 1, GetNumGroupMembers() do
            local unit = self:Get("raid" .. i)
            if unit.exists and unit.guid ~= tank.guid and 
               unit.role == "TANK" then
                return unit
            end
        end
    end
    return self:Get("none")
end)


Emergency Healing
local criticalHealth = Aurora.UnitManager:RegisterVirtualUnit("criticalHealth", function(self)
    local critical = nil
    local lowestHP = 30 -- Critical threshold
    
    Aurora.fgroup:each(function(unit)
        if unit.alive and unit.hp < lowestHP then
            critical = unit
            lowestHP = unit.hp
        end
        return false
    end)
    
    return critical or self:Get("none")
end)

--
Spell Overview
The Spell class provides a comprehensive interface for handling spells in World of Warcraft. It includes functionality for checking spell availability, casting spells, managing cooldowns, and handling various spell-specific behaviors.

Important Note About Checks
Several checks are automatically performed in the cast() and smartaoe() functions, making manual checks redundant. These include:

ready() - No need to check if spell is ready before casting
castable(unit) - No need to check if spell is castable before casting
isusable() - No need to check if spell is usable before casting
inrange(unit) - No need to check range before casting
unit.distance - No need to check distance before casting
unit.los - No need to check line of sight before casting
unit.facing - No need to check facing before casting
Incorrect Usage:

if spell:ready() and spell:castable("target") and target.los and target.distanceto(player) < 40 then
    spell:cast("target") -- Redundant checks!
end


Correct Usage:

spell:cast("target") -- All necessary checks are performed internally


Installation
local spell = Aurora.SpellHandler.NewSpell(spellID, payload)


Parameters
Parameter	Type	Description
spellID	number | number[]	Single spell ID or array of spell IDs for different ranks
payload	table	Optional configuration settings

--
Gets remaining cooldown time in seconds.

local cooldown = spell:getcd() -- Returns number (seconds)

charges()
Gets current number of charges.

local currentCharges = spell:charges() -- Returns number

maxcharges()
Gets maximum number of charges.

local maxCharges = spell:maxcharges() -- Returns number

chargesleft()
Gets fractional charges remaining (includes partial charge regeneration).

local fractionalCharges = spell:chargesleft() -- Returns number


timetofull()
Gets time until all charges are regenerated.

local timeToFull = spell:timetofull() -- Returns number (seconds)


timetonextcharge()
Gets time until next charge is available.

local timeToNext = spell:timetonextcharge() -- Returns number (seconds)


Cast History Methods
wasLastCast(timeWindow)
Checks if this spell was the last one cast within the specified time window.

local wasLast = spell:wasLastCast(1.5) -- Returns boolean

wasSecondLastCast()
Checks if this spell was the second-to-last spell cast.

local wasSecondLast = spell:wasSecondLastCast() -- Returns boolean


timeSinceLastCast()
Gets time elapsed since this spell was last cast.

local timeSince = spell:timeSinceLastCast() -- Returns number (seconds)


AOE Methods
smartaoe(target, options)
Intelligently casts AOE spell considering multiple targets.

spell:smartaoe(target, {
    offsetMin = 0,         -- Minimum offset distance
    offsetMax = 8,         -- Maximum offset distance
    distanceSteps = 24,    -- Number of distance checks
    circleSteps = 48,      -- Number of circular positions to check
    filter = function(unit, distance, position) -- Optional filter function
        return true -- Return true to count this unit
    end,
    ignoreEnemies = false, -- Ignore enemy units
    ignoreFriends = false  -- Ignore friendly units
})


smartaoeposition(target, options)
Gets the optimal position for an AOE spell cast.

local position = spell:smartaoeposition(target, {
    -- Same options as smartaoe()
})
-- Returns {x, y, z, hitCount} or nil

Utility Methods
inrange(unit)
Checks if target is within spell range.

local inRange = spell:inrange(target) -- Returns boolean

rank()
Gets the current rank of a talent spell.

local rank = spell:rank() -- Returns number

overlayed()
Checks if the spell is currently overlayed (glowing).

local isOverlayed = spell:overlayed() -- Returns boolean

getcasttime()
Gets the cast time of the spell in seconds.

local castTime = spell:getcasttime() -- Returns number (seconds)


isusable()
Checks if spell is currently usable (has resources, etc).

local isusable, notEnoughResources = spell:isusable() -- Returns two booleans


Example Usage
-- Create a new spell object for Fireball
local fireball = Aurora.SpellHandler.NewSpell(133, {
})

-- Check if we can cast Fireball on our target
if fireball:castable("target") then
    -- Cast Fireball
    fireball:cast("target")
end

-- Create an AOE spell like Blizzard
local blizzard = Aurora.SpellHandler.NewSpell(190356, {
    isSkillshot = true,
    radius = 8
})

-- Cast Blizzard optimally on groups of enemies
blizzard:smartaoe("target", {
    offsetMax = 30,
    filter = function(unit, distance, position)
        return unit.enemy and not unit.dead
    end
})

--
pell Payload
When creating a new spell, you can configure its behavior using the payload table. Here are all available options:

Payload Options
Option	Type	Default	Description
ignoreCasting	boolean	false	Ignore if player is casting
ignoreChanneling	boolean	false	Ignore if player is channeling
ignoreCost	boolean	false	Ignore resource costs
ignoreFacing	boolean	false	Ignore facing requirements
ignoreMoving	boolean	false	Ignore movement restrictions
isSkillshot	boolean	false	Treat as skillshot spell
maxOffset	number	0	Maximum targeting offset
minOffset	number	0	Minimum targeting offset
nextMelee	boolean	false	Queue for next melee
radius	number	0	Spell effect radius
queued	boolean	false	Allow spell queueing
timeToHit	number	0	Time until spell impact
magicDispel	boolean	false	Can dispel magic
curseDispel	boolean	false	Can dispel curses
poisonDispel	boolean	false	Can dispel poison
diseaseDispel	boolean	false	Can dispel disease
Example Usage
local spell = Aurora.SpellHandler.NewSpell(spellID, {
    ignoreFacing = true,
    ignoreMoving = true,
    isSkillshot = true,
    radius = 8,
    maxOffset = 30
})

--
Spell Methods
Core Methods
cast(unit)
Attempts to cast the spell on the specified unit.

local success = spell:cast(target) -- Returns boolean indicating success


castable(unit)
Checks if spell can be cast on the specified unit.

local canCast = spell:castable(target) -- Returns boolean

ready()
Checks if spell is ready to be cast (off cooldown and usable).

local isReady = spell:ready() -- Returns boolean

Cooldown Methods
getcd()
Gets remaining cooldown time in seconds.

local cooldown = spell:getcd() -- Returns number (seconds)

charges()
Gets current number of charges.

local currentCharges = spell:charges() -- Returns number

maxcharges()
Gets maximum number of charges.

local maxCharges = spell:maxcharges() -- Returns number

chargesleft()
Gets fractional charges remaining (includes partial charge regeneration).

local fractionalCharges = spell:chargesleft() -- Returns number


timetofull()
Gets time until all charges are regenerated.

local timeToFull = spell:timetofull() -- Returns number (seconds)


timetonextcharge()
Gets time until next charge is available.

local timeToNext = spell:timetonextcharge() -- Returns number (seconds)


Cast History Methods
wasLastCast(timeWindow)
Checks if this spell was the last one cast within the specified time window.

local wasLast = spell:wasLastCast(1.5) -- Returns boolean

wasSecondLastCast()
Checks if this spell was the second-to-last spell cast.

local wasSecondLast = spell:wasSecondLastCast() -- Returns boolean


timeSinceLastCast()
Gets time elapsed since this spell was last cast.

local timeSince = spell:timeSinceLastCast() -- Returns number (seconds)


AOE Methods
smartaoe(target, options)
Intelligently casts AOE spell considering multiple targets.

spell:smartaoe(target, {
    offsetMin = 0,         -- Minimum offset distance
    offsetMax = 8,         -- Maximum offset distance
    distanceSteps = 24,    -- Number of distance checks
    circleSteps = 48,      -- Number of circular positions to check
    filter = function(unit, distance, position) -- Optional filter function
        return true -- Return true to count this unit
    end,
    ignoreEnemies = false, -- Ignore enemy units
    ignoreFriends = false  -- Ignore friendly units
})


smartaoeposition(target, options)
Gets the optimal position for an AOE spell cast.

local position = spell:smartaoeposition(target, {
    -- Same options as smartaoe()
})
-- Returns {x, y, z, hitCount} or nil

Utility Methods
inrange(unit)
Checks if target is within spell range.

local inRange = spell:inrange(target) -- Returns boolean

rank()
Gets the current rank of a talent spell.

local rank = spell:rank() -- Returns number

overlayed()
Checks if the spell is currently overlayed (glowing).

local isOverlayed = spell:overlayed() -- Returns boolean

getcasttime()
Gets the cast time of the spell in seconds.

local castTime = spell:getcasttime() -- Returns number (seconds)


isknown()
Checks if the spell/talent is known by the player.

local isKnown = spell:isknown() -- Returns boolean

isusable()
Checks if spell is currently usable (has resources, etc).

local isusable, notEnoughResources = spell:isusable() -- Returns two booleans


Complete Example
-- Create a new spell object for Fireball
local fireball = Aurora.SpellHandler.NewSpell(133, {
})

-- Cast Fireball
fireball:cast("target")

-- Create an AOE spell like Blizzard
local blizzard = Aurora.SpellHandler.NewSpell(190356, {
    isSkillshot = true,
    radius = 8
})

-- Cast Blizzard optimally on groups of enemies
blizzard:smartaoe("target", {
    offsetMax = 30,
    filter = function(unit, distance, position)
        return unit.enemy and not unit.dead
    end
})

--
Missile System Overview
The Missile system provides tracking and information about spell projectiles in the game. This includes abilities like Fireball, Ice Lance, or any other visible spell projectile.

Accessing Missiles

-- Get all active missiles
Aurora.missiles:each(function(missile)
    -- Work with each missile
end)


-- Get missiles from a specific unit
local player = Aurora.UnitManager:Get("player")
Aurora.missiles:each(function(missile)
    if missile.creator == player then
        -- Work with player's missiles
    end
end)

Basic Properties
missile.spellid           -- ID of the spell that created the missile
missile.creator          -- Unit that created the missile
missile.target           -- Target unit of the missile
missile.progress         -- Percentage of journey completed (0-100)
missile.distancetraveled -- Distance traveled so far


Next Steps
Learn about Missile Properties

--
Missile Properties
Position Properties
Initial Position
missile.ix  -- Initial X coordinate
missile.iy  -- Initial Y coordinate
missile.iz  -- Initial Z coordinate
-- Or use:
missile.initialposition -- Returns {x, y, z} table

Current Position
missile.cx  -- Current X coordinate
missile.cy  -- Current Y coordinate
missile.cz  -- Current Z coordinate
-- Or use:
missile.currentposition -- Returns {x, y, z} table

Model Position
missile.mx  -- Model X coordinate
missile.my  -- Model Y coordinate
missile.mz  -- Model Z coordinate
-- Or use:
missile.modelposition -- Returns {x, y, z} table

Hit Position
missile.hx  -- Hit X coordinate
missile.hy  -- Hit Y coordinate
missile.hz  -- Hit Z coordinate
-- Or use:
missile.hitposition -- Returns {x, y, z} table

Distance Properties
missile.distancetraveled  -- Distance traveled so far
missile.distanceremaining -- Distance left to target
missile.totaldistance     -- Total distance from start to end
missile.progress          -- Percentage of journey completed (0-100)


Unit Properties
missile.creator  -- Unit that created the missile
missile.target   -- Target unit of the missile
missile.source   -- Source GUID

Spell Properties
missile.spellid  -- ID of the spell that created the missile
missile.id       -- Object ID of the missile

--

Misc
--
Draw
The Draw utility provides functionality for rendering visual elements in the game world. It's built on top of Tinkr's Draw utility and provides additional features for color management and callback-based drawing.

Basic Usage
local Draw = Aurora.Draw

-- Register a drawing callback
Draw:RegisterCallback("myDrawing", function(canvas, unit)
    -- Drawing code here
end, "units")

Callback Registration
RegisterCallback
Register a drawing callback for units, objects, or both.

Draw:RegisterCallback(name, callback, targetType)

name: Unique identifier for the callback
callback: Function that will be called for drawing
targetType: "units" | "objects" | "both" (default: "both")
UnregisterCallback
Remove a previously registered callback.

Draw:UnregisterCallback(name)

Drawing Methods
Atlas
Draw a texture from the game's atlas.

Draw:Atlas(atlasName, x, y, z, width, height, alpha, scale)

Example:

Draw:Atlas("Mobile-QuestIcon", unitPos.x, unitPos.y, unitPos.z + 3, 50, 50, 1, 0.4)


Color Management
GetColor
Get RGB values for predefined colors.

local r, g, b, a = Draw:GetColor(colorName, opacity)

Available Colors:

-- Basic Colors
"Red"     -- RGB(255, 0, 0)
"Green"   -- RGB(0, 255, 0)
"Blue"    -- RGB(0, 0, 255)
"Yellow"  -- RGB(254, 199, 74)
"Orange"  -- RGB(255, 165, 0)
"Brown"   -- RGB(205, 133, 63)
"Text"    -- RGB(255, 255, 255)

-- Class Colors
"Deathknight"  -- RGB(196, 30, 58)
"Demonhunter"  -- RGB(163, 48, 201)
"Druid"        -- RGB(255, 124, 10)
"Evoker"       -- RGB(51, 147, 127)
"Hunter"       -- RGB(170, 211, 114)
"Mage"         -- RGB(63, 199, 235)
"Monk"         -- RGB(0, 255, 152)
"Paladin"      -- RGB(244, 140, 186)
"Priest"       -- RGB(255, 255, 255)
"Rogue"        -- RGB(255, 244, 104)
"Shaman"       -- RGB(0, 112, 221)
"Warlock"      -- RGB(135, 136, 238)
"Warrior"      -- RGB(198, 155, 109)

-- Special
"Rainbow"      -- Cycling RGB colors

Examples
Drawing Unit Markers
Draw:RegisterCallback("unitMarkers", function(canvas, unit)
    if unit.enemy and unit.alive then
        -- Draw red circle for enemies
        local r, g, b, a = Draw:GetColor("Red", 70)
        canvas:SetColor(r, g, b, a)
        canvas:Circle(unit.position.x, unit.position.y, unit.position.z, 1)
    end
end, "units")


Class-Colored Names
Draw:RegisterCallback("classNames", function(canvas, unit)
    if unit.player then
        local r, g, b, a = Draw:GetColor(unit.class2, 255)
        canvas:SetColor(r, g, b, a)
        canvas:Text(unit.name,"GameFontHighlight", unit.position.x, unit.position.y, unit.position.z + 2)
    end
end, "units")


Best Practices
Performance
Minimize the number of draw operations in callbacks
Use appropriate target types to avoid unnecessary iterations
Cache color values if using them frequently
Remove callbacks when they're no longer needed
Common Pitfalls
Don't create new vectors or perform heavy calculations in draw callbacks
Be mindful of draw operation stacking and opacity
Consider distance and visibility for drawing operations
Remember that drawing happens every frame
Notes
Draw Updates
Drawing callbacks are executed every frame
Drawing is disabled while resting
The Draw utility must be enabled with Draw:Enable()
Color Management
Colors are normalized to 0-255 range
Opacity is optional and defaults to 90
Class colors are automatically matched to WoW standards
Rainbow color updates automatically
Tinkr's Native Drawing API
Click to view all available drawing methods
Tinkr's Native Drawing API
Click to view all available drawing methods
Coordinate and Camera Methods
-- Convert world coordinates to screen coordinates
Draw:WorldToScreen(wx, wy, wz)

-- Get current camera position
Draw:CameraPosition()

-- Map a value from one range to another
Draw:Map(value, fromLow, fromHigh, toLow, toHigh)

Color Management
-- Set color with normalized values (0-1)
Draw:SetColor(r, g, b, a)

-- Set color with raw values (0-255)
Draw:SetColorRaw(r, g, b, a)

-- Set alpha value
Draw:SetAlpha(a)

-- Convert hex color to RGB
Draw:HexToRGB(hex)

-- Set/Get color from object
Draw:SetColorFromObject(object)
Draw:GetColorFromObject(object)

Distance and Measurements
-- Calculate 3D distance between points
Draw:Distance(ax, ay, az, bx, by, bz)

-- Calculate 2D distance between points
Draw:Distance2D(x1, y1, x2, y2)

-- Set line width
Draw:SetWidth(width)

Rotation Methods
-- Rotate around X axis
Draw:RotateX(cx, cy, cz, px, py, pz, r)

-- Rotate around Y axis
Draw:RotateY(cx, cy, cz, px, py, pz, r)

-- Rotate around Z axis
Draw:RotateZ(cx, cy, cz, px, py, pz, r)

Drawing Primitives
-- Draw line with distance check
Draw:Line(x1, y1, z1, x2, y2, z2, maxD)

-- Draw line without distance check
Draw:LineRaw(x1, y1, z1, x2, y2, z2)

-- Draw 2D line
Draw:Line2D(sx, sy, ex, ey)

-- Draw circle
Draw:Circle(x, y, z, radius, steps)

-- Draw cylinder
Draw:Cylinder(x, y, z, radius, height)

-- Draw array of vectors
Draw:Array(vectors, x, y, z, rotationX, rotationY, rotationZ)

-- Draw text
Draw:Text(text, font, x, y, z)

-- Draw texture
Draw:Texture(config, x, y, z, alphaA)

-- Draw arc
Draw:Arc(x, y, z, size, arc, rotation)

-- Draw rectangle
Draw:Rectangle(x, y, z, w, l, rot)


Canvas Control
-- Clear the canvas
Draw:ClearCanvas()

-- Update the canvas
Draw:Update()

-- Show helper grid
Draw:Helper()

-- Enable drawing
Draw:Enable()

-- Disable drawing
Draw:Disable()

-- Check if drawing is enabled
Draw:Enabled()

-- Register sync callback
Draw:Sync(callback)

-- Create new canvas
Draw:New(canvas)


Using Native Methods
The native drawing methods provide lower-level access to the drawing system. They're useful when you need:

Precise control over coordinates and transformations
Custom shapes and patterns
Performance optimization for complex drawings
Direct manipulation of the canvas
Callback vs Canvas Management
Recommended: Single Canvas, Multiple Callbacks
-- Multiple callbacks sharing one canvas
Draw:RegisterCallback("enemies", function(canvas, unit)
    if unit.enemy then
        canvas:Circle(unit.position.x, unit.position.y, unit.position.z, 1)
    end
end, "units")

Draw:RegisterCallback("friends", function(canvas, unit)
    if unit.friendly then
        canvas:Text(unit.name, "GameFontNormal", unit.position.x, unit.position.y, unit.position.z)
    end
end, "units")


✅ Better performance, shared canvas, easy feature management

Not Recommended: Multiple Canvases
-- Separate canvas per feature
local enemyCanvas = Tinkr.Util.Draw:New()
enemyCanvas:Sync(function(self)
    Aurora.ObjectManager.units:each(function(unit)
        if unit.enemy then
            self:Circle(unit.position.x, unit.position.y, unit.position.z, 1)
        end
    end)
end)


❌ Higher memory usage, redundant loops, complex management

Performance
Cache frequently used values (position, enemy, etc.)
Group similar operations (same color, same type)
Use early returns for invalid states
Avoid creating objects in callbacks

--
Macro System
The Macro system provides a way to create and manage slash commands in the game. It allows you to register custom commands that can be executed through chat.

Basic Usage
First Run
On first run, you'll be prompted to set a prefix via a GUI window. This preference is saved for future sessions.

local Macro = Aurora.Macro

-- Register a simple command
Macro:RegisterCommand("hello", function(name)
    print("Hello, " .. (name or "stranger") .. "!")
end, "Greets a player")

Command Registration
RegisterCommand
Macro:RegisterCommand(command, callback, description)

command: String name for the command
callback: Function to execute when command is called
description: Optional description for help text
Examples
Basic Command
-- Creates /aurora greet [name]
Macro:RegisterCommand("greet", function(name)
    print("Hello, " .. (name or "stranger") .. "!")
end, "Greets a player")

Command with Arguments
-- Creates /aurora cast [spell]
Macro:RegisterCommand("cast", function(spell)
    if spell then
        Aurora.Spell:Cast(spell)
    end
end, "Casts the specified spell")

Help Command
The help command can be accessed in two ways:

/aurora          -- Lists all available commands
/aurora help     -- Same as above

Both commands will display a list of all registered commands with their descriptions in the format:

/aurora commandName - Command description

Best Practices
Command Design
Use clear, descriptive command names
Always provide a helpful description
Handle missing arguments gracefully
Keep commands simple and focused
Common Pitfalls
Avoid command names that might conflict with other addons
Don't register commands in performance-critical code
Remember to handle all possible argument cases

--

Event Handler
The Event Handler provides a streamlined way to handle both combat log events and normal WoW events. It offers filtering capabilities and structured event data.

Basic Usage
local EventHandler = Aurora.EventHandler

-- Register a combat log event handler
EventHandler:RegisterEvent("SPELL_CAST_SUCCESS", function(eventData)
    if eventData.source.guid == UnitGUID("player") then
        print(string.format("You cast %s", C_Spell.GetSpellLink(eventData.params[1])))
    end
end)

-- Register a normal WoW event handler
EventHandler:RegisterNormalEvent("PLAYER_ENTERING_WORLD", function()
    print("Player entered the world")
end)


Event Registration
Combat Log Events
EventHandler:RegisterEvent(eventType, handlerFunction)

eventType: Combat log event type (e.g., "SPELL_CAST_SUCCESS")
handlerFunction: Function that receives the structured event data
Normal Events
EventHandler:RegisterNormalEvent(eventType, handlerFunction)


eventType: WoW event name (e.g., "PLAYER_ENTERING_WORLD")
handlerFunction: Function that receives the raw event parameters
Event Data Structure
Combat log events provide structured data:

eventData = {
    timestamp = 1234567890,
    event = "SPELL_CAST_SUCCESS",
    source = {
        guid = "Player-1234-5678",
        name = "PlayerName",
        flags = sourceFlags,
        raidFlags = sourceRaidFlags
    },
    dest = {
        guid = "Target-1234-5678",
        name = "TargetName",
        flags = destFlags,
        raidFlags = destRaidFlags
    },
    params = { spellId, spellName, ... } -- Additional event-specific parameters
}


Event Filtering
Add filters to process only specific events:

-- Only process events where the player is the source
EventHandler:AddFilter("SPELL_CAST_SUCCESS", function(eventData)
    return eventData.source.guid == UnitGUID("player")
end)


Examples
Track Player Spells
EventHandler:RegisterEvent("SPELL_CAST_SUCCESS", function(eventData)
    if eventData.source.guid == UnitGUID("player") then
        local spellId, spellName = unpack(eventData.params)
        print(string.format("Cast %s (ID: %d)", spellName, spellId))
    end
end)


Monitor Interrupts
EventHandler:RegisterEvent("SPELL_INTERRUPT", function(eventData)
    local _, _, _, extraSpellId, extraSpellName = unpack(eventData.params)
    print(string.format("%s interrupted %s's %s", 
        eventData.source.name,
        eventData.dest.name,
        extraSpellName))
end)


Track Group Changes
EventHandler:RegisterNormalEvent("GROUP_ROSTER_UPDATE", function()
    print("Group composition changed")
end)


Best Practices
Performance
Use filters to reduce unnecessary event processing
Keep event handlers lightweight
Consider batching frequent events
Clean up handlers when no longer needed
Common Pitfalls
Don't register too many handlers for the same event
Be careful with string operations in high-frequency events
Remember that some events fire very frequently
Handle nil cases in event data
Common Combat Log Events
Click to view common combat log events
Event Processing
Combat log events provide more structured data than normal events

--

Toast Notifications
The Toast system provides elegant, non-intrusive notifications that appear temporarily on your screen.

Features
Configurable position (top-right, top-left, bottom-right, bottom-left)
Ability to hide notifications completely
Toast Example


Basic Usage
Aurora.Toast:Show("Title", "Message")

Example
-- Show a welcome message
local playerName = UnitName("player")
Aurora.Toast:Show(
    string.format("Welcome, %s!", playerName),
    "Type /aurora for settings"
)

Configuration
Position
You can configure the toast position in the Aurora settings under the "General" tab. Available positions:

Top Right
Top Left
Bottom Right (default)
Bottom Left
Hidden (disables notifications)
Structure
Each toast notification consists of:

Aurora branding (top-left)
Title (below branding)
Message (main content)
API Reference
Methods
Toast:Show(title, message)
Shows a new toast notification.

Parameters:
title: string - The toast title
message: string - The toast message
Returns: void

--

StatusFrame
Documentation for the StatusFrame UI component, which provides a movable frame with toggle buttons for controlling various aspects of your rotation or addon functionality.

Status Frame
The Status Frame provides a customizable interface for creating toggle buttons with icons. Aurora comes with a global status frame that includes common toggles like Rotation, Cooldown, and Interrupt controls.

Status Frame

Using the Global Status Frame
The global status frame is automatically initialized and provides a set of default toggles. You can access these default toggles through Aurora.Rotation:

-- Default global toggles
Aurora.Rotation.Toggle    -- Main rotation toggle
Aurora.Rotation.Cooldown  -- Cooldown usage toggle
Aurora.Rotation.Interrupt -- Interrupt toggle

Adding Custom Toggles
You can add your own toggles to the global status frame using Aurora:AddGlobalToggle():

local myToggle = Aurora:AddGlobalToggle({
    label = "AoE:",              -- Display name (max 11 characters)
    var = "my_aoe_toggle",       -- Unique identifier for saving state
    icon = "Interface/Icons/Spell_Holy_HolyNova", -- Icon texture or spell ID
    tooltip = "Toggle AoE mode", -- Tooltip text
    onClick = function(value)    -- Optional callback when clicked
        print("AoE mode:", value)
    end
})

-- Later you can check the toggle state
if myToggle:GetValue() then
    -- AoE mode is enabled
end


Toggle Options
Option	Type	Description
label	string	Display text (max 11 chars)
var	string	Unique identifier for saving state
icon	string/number	Icon texture path or spell ID
tooltip	string	Hover tooltip text
onClick	function	Callback function when clicked
Icon Sources
Icons can be specified in two ways:

Texture Path: Direct path to the icon texture

icon = "Interface/Icons/Spell_Nature_Lightning"

Spell ID: Numeric spell ID that will use that spell's icon

icon = 48108  -- Will use Pyroblast's icon

Controlling Toggles
Toggles provide methods to control their state:

-- Get current value
local isEnabled = myToggle:GetValue()

-- Set value programmatically
myToggle:SetValue(true)

-- Update tooltip text
myToggle:SetCustomText("New tooltip text")

State Persistence
Toggle states are automatically saved between sessions. The saved state is restored when the toggle is recreated with the same var name.

Example: Class-Specific Toggles
Here's an example of adding class-specific toggles to a rotation:

    Aurora.Rotation.BurstToggle = Aurora:AddGlobalToggle({
        label = "Burst",
        var = "my_burst_toggle",
        icon = "Interface/Icons/Ability_Warrior_BattleShout",
        tooltip = "Enable burst mode rotation"
    })
    Aurora.Rotation.DefensiveToggle = Aurora:AddGlobalToggle({
        label = "Defensive",
        var = "my_defensive_toggle",
        icon = "Interface/Icons/Ability_Warrior_DefensiveStance",
        tooltip = "Use defensive cooldowns"
    })
end

if Aurora.Rotation.DefensiveToggle:GetValue() then
    -- Do Defensives
end


tip
Keep toggle labels short and descriptive. The maximum length is 11 characters, and shorter labels often look better.

note
All toggles are saved automatically and will remember their state between game sessions.

--

Alert System
Documentation for the Alert System (Toast Notifications), which provides animated notifications with icons and text for your Rotation.

Alert Example
Alert System Basics
The Alert System (Toast Notifications) provides animated notifications with icons and text that appear at the top of the screen. It's perfect for displaying important information, spell procs, or status updates to the player.

Basic Usage
The simplest way to show an alert is:

-- Show a simple text alert
Aurora.alert("Your message here")

-- Show an alert with a spell icon
Aurora.alert("Spell Ready!", 12345)  -- Replace 12345 with your spell ID


Advanced Usage
You can customize the alert appearance and behavior:

-- Customized alert with timing and payload
Aurora.alert({
    string = "Critical Hit!",
    time = 3,           -- Display for 3 seconds
    fadeTime = 0.7,     -- Fade out over 0.7 seconds
    fadeInTime = 0.2    -- Fade in over 0.2 seconds
}, "Interface\\Icons\\ability_warrior_rampage", {
    soundID = 12345,              -- Play a sound
    iconSizeOverride = 40,        -- Custom icon size
    circularMaskOverride = true   -- Force circular icon mask
})


Features
Animated Transitions: Smooth fade in/out and scaling animations
Multiple Alerts: Stack multiple alerts with automatic management
Icon Support: Display spell icons or custom textures
Sound Effects: Play sounds with notifications
Customizable: Extensive configuration options
Auto-cleanup: Automatic removal of expired alerts
Best Practices
Keep Messages Short: Alerts are best for brief, important messages
Use Icons Wisely: Icons help users quickly identify the alert type
Don't Spam: Avoid showing too many alerts in quick succession
Sound Usage: Use sounds sparingly and only for important alerts
Examples
Here are some examples of how you can use the Alert System:

-- Proc alert with spell icon
Aurora.alert("Bloodlust Active!", 2825)

-- Custom duration alert
Aurora.alert({
    string = "Boss Incoming!",
    time = 5,  -- Show for 5 seconds
}, "Interface\\Icons\\ability_warrior_charge")

-- Alert with sound
Aurora.alert("Level Up!", "Interface\\Icons\\achievement_level_80", {
    soundID = 888  -- Level up sound
}) 
--


Utility Functions
Documentation for Aurora utility functions that help with rotation development.

--

Utility Functions
Documentation for Aurora utility functions that help with rotation development.

--
Frame and Callback System
Aurora provides a robust callback system for timed execution of code. This system optimizes performance by managing update frequencies and staggering callbacks to prevent frame rate drops.

Callback Types
Aurora offers two main types of callbacks:

Update Callbacks: Run at a fixed 0.1-second interval
Tick Callbacks: Used for more precisely timed operations
Registration Methods
Aurora:OnUpdate(callback, enabled)
Registers a function to be called approximately every 0.1 seconds.

-- Parameters:
-- callback: function(elapsed) - Function to call with elapsed time parameter
-- enabled: boolean - Whether the callback starts enabled (default: true)
-- Returns: number - Unique ID for the callback

-- Example:
local updateId = Aurora:OnUpdate(function(elapsed)
    -- Code to run every 0.1 seconds
    print("Time elapsed: " .. elapsed)
end)


The framework automatically staggers update callbacks by assigning each one a small offset (0-0.09 seconds) to distribute processing load and prevent all callbacks from executing in the same frame.

Aurora:OnTick(callback, enabled)
Registers a function to be called on tick intervals (used for more precise timing operations).

-- Parameters:
-- callback: function(elapsed) - Function to call with elapsed time parameter
-- enabled: boolean - Whether the callback starts enabled (default: true)
-- Returns: number - Unique ID for the callback

-- Example:
local tickId = Aurora:OnTick(function(elapsed)
    -- Code that needs precise timing
    if player.casting then
        -- Track casting progress
    end
end)


Best Practices
Performance Optimization
Use OnUpdate for Non-Critical Operations:

Interface updates
Status checks
Data collection
Use OnTick for Time-Sensitive Operations:

Cast tracking
Interrupt timing
Precise rotation logic
Enable/Disable as Needed:

-- Store callback reference
local myCallbackId

-- Register with disabled state
myCallbackId = Aurora:OnUpdate(function(elapsed)
    -- Heavy processing here
end, false)

-- Enable only when needed
if inCombat then
    Aurora.updateCallbacks[myCallbackId].enabled = true
else
    Aurora.updateCallbacks[myCallbackId].enabled = false
end


Memory Management
Always remove callbacks that are no longer needed:

-- When a module is disabled or no longer needs the callback
Aurora:RemoveCallback(callbackId, true)


Notes
warning
Avoid excessive processing in update callbacks. Keep operations light and efficient to prevent frame rate drops.

--
Interface
Documentation for the Interface and GUI Builder system

GUI Builder Overview
The GUI Builder provides a fluent interface for creating configuration UIs in World of Warcraft. It supports various UI elements like buttons, checkboxes, sliders, and dropdowns, organized in categories and tabs.

Basic Structure
local gui = Aurora.GuiBuilder:New()
gui:Category("My Category")
   :Tab("General")
   :Header({ text = "Settings" })
   :Checkbox({ text = "Enable Feature" })
   :Slider({ text = "Speed" })

Key Features
Fluent interface for easy UI creation
Automatic configuration saving/loading
Profile system integration
Organized by categories and tabs
Various UI elements available
Next Steps
Explore UI Elements
Study Configuration Integration
Learn about Configuration System

--
UI Elements
Important
Always provide a key parameter if you want the element's value to be saved and loaded between sessions. Without a key, the element will reset to its default value when reloading the UI.

Adding Icons to Text
You can use Aurora.texture() to add spell icons or custom textures to your text:

-- Using spell ID (automatically gets spell icon)
local fireballIcon = Aurora.texture(133) -- Fireball spell ID

-- Using custom texture path
local customIcon = Aurora.texture("Interface\\Icons\\Ability_Warrior_Charge")

-- Specify custom size (default is 14)
local largeIcon = Aurora.texture(133, 20)

-- Use in UI elements
gui:Header({
    text = fireballIcon .. " Fire Spells"
})

gui:Button({
    text = customIcon .. " Charge Settings"
})


Button
gui:Button({
    text = "Click Me",
    width = 120,      -- Optional
    height = 25,      -- Optional
    tooltip = "Click this button to do something", -- Optional tooltip
    onClick = function() 
        print("clicked") 
    end
})


Checkbox
gui:Checkbox({
    text = "Enable Feature",
    key = "feature.enabled",  -- Config key for saving
    default = false,          -- Default value
    tooltip = "Enable this feature to do something cool", -- Optional tooltip
    onChange = function(self, checked)
        print("Checkbox changed:", checked)
    end
})


Slider
gui:Slider({
    text = "Speed",
    key = "speed.value",
    min = 0,
    max = 100,
    step = 1,
    default = 50,
    tooltip = "Adjust the speed of the animation", -- Optional tooltip
    onChange = function(self, value)
        print("Speed changed:", value)
    end
})


Dropdown
gui:Dropdown({
    text = "Quality",
    key = "graphics.quality",
    options = {
        { text = "Low", value = "low" },
        { text = "Medium", value = "medium" },
        { text = "High", value = "high" }
    },
    default = "medium",
    multi = false,           -- Set to true for multi-select
    width = 200,            -- Optional
    tooltip = "Select quality level",
    onChange = function(self, value)
        print("Quality changed:", value)
    end
})


Header
gui:Header({
    text = "Section Title"
})

Half Label
gui:HalfLabel({
    text = "Left Side"
})

Spacer
gui:Spacer()  -- Adds empty space 

ColorPicker
gui:ColorPicker({
    text = "Text Color",
    key = "ui.textColor",    -- Config key for saving
    default = {r = 1, g = 0, b = 0, a = 1},  -- Default to red
    width = 200,             -- Optional
    height = 20,             -- Optional
    tooltip = "Choose the color for UI text",
    onChange = function(self, color)
        print("Color changed:", color.r, color.g, color.b, color.a)
        -- Example: Apply the color
        -- MyAddonFrame.text:SetTextColor(color.r, color.g, color.b, color.a)
    end
})


DoubleSlider
gui:DoubleSlider({
    text1 = "Min Health",    -- Label for first slider
    text2 = "Max Health",    -- Label for second slider
    key = "healing.range",   -- Base key for saving (will append .value1 and .value2)
    min1 = 0,                -- Minimum value for first slider
    max1 = 100,              -- Maximum value for first slider
    min2 = 0,                -- Minimum value for second slider
    max2 = 100,              -- Maximum value for second slider
    default1 = 30,           -- Default value for first slider
    default2 = 80,           -- Default value for second slider
    step = 1,                -- Default step size for both sliders
    step1 = 5,               -- Optional: Custom step for first slider
    step2 = 5,               -- Optional: Custom step for second slider
    tooltip = "Set the health percentage range for healing spells",
    onChange = function(self, value1, value2)
        print("Range changed:", value1, "to", value2)
    end
})


This creates two sliders that can be used to set a minimum and maximum value, perfect for defining ranges like health thresholds, distance limits, or time intervals.

Sliders with Different Units
You can use the DoubleSlider when you need to set two related values that may use different units or scales:

gui:DoubleSlider({
    text1 = "Distance",
    text2 = "Time Limit",
    key = "movement.parameters",
    min1 = 0,
    max1 = 40,  -- Distance in yards
    min2 = 0,
    max2 = 10,  -- Time in seconds
    default1 = 20,
    default2 = 3,
    tooltip = "Configure distance and time limit for movement abilities"
})


Tooltips
Every UI element can have a tooltip that appears when hovering over it. Just add the tooltip parameter to any element:

gui:Button({
    text = "My Button",
    tooltip = "This tooltip explains what the button does"
})


Hotkey
gui:Hotkey({
    text = "Toggle",
    key = "toggleKey",    -- Config key for saving
    default = "F1",          -- Default key binding
    tooltip = "Click to set a key binding for toggling the bot",
})


The Hotkey element creates a button that captures keyboard input to define key bindings. Users can click the button to start binding mode, then press any key combination (including modifier keys like Shift, Alt, and Ctrl).

-- Load saved hotkey from config
local binding = Aurora.Config:Read("myAbilityHotkey")

-- Register it with the KeyBindingSystem
if binding and binding ~= "" then
    Aurora.KeyBindingSystem:RegisterWoWHotkey(binding, function(isPressed)
        if isPressed then
            print("My ability activated!")
            -- Your ability code here
        end
    end)
end

--

Configuration Integration
The GUI Builder automatically integrates with Aurora's configuration system when you provide a key parameter to UI elements.

Key Required for Persistence
Without a key parameter, element values will not persist between sessions. Always provide a key if you want to save the value.

-- Value will NOT persist (resets on reload)
gui:Checkbox({
    text = "Feature",
    default = false
})

-- Value WILL persist
gui:Checkbox({
    text = "Feature",
    key = "feature.enabled", -- Key is required for persistence
    default = false
})


Saving and Loading
gui:Checkbox({
    text = "Enable Feature",
    key = "feature.enabled",  -- Config key
    default = false          -- Default value
})

When a key is provided:

The value is automatically loaded from saved configuration
Changes are automatically saved
The value persists between sessions
Profile system integration is automatic
Profile System
The GUI Builder automatically integrates with the profile system:

Values update when profiles change
Changes are saved to the current profile
Default values are used for new profiles
Example with Multiple Settings
gui:Category("Graphics")
   :Tab("Quality")
   :Checkbox({
        text = "Enable Shadows",
        key = "graphics.shadows",
        default = true
   })
   :Slider({
        text = "View Distance",
        key = "graphics.viewDistance",
        min = 1,
        max = 10,
        default = 5
   })
   :Dropdown({
        text = "Texture Quality",
        key = "graphics.textures",
        options = {
            { text = "Low", value = "low" },
            { text = "High", value = "high" }
        },
        default = "high"
   })

--

Configuration System
Aurora provides a simple configuration system for reading and writing settings.

Accessing Values
Reading Values

-- Read a value (returns default if not set)
local value = Aurora.Config:Read("myFeature.enabled")

Writing Values
-- Save a value
Aurora.Config:Write("myFeature.enabled", true)

-- Save multiple values
Aurora.Config:Write("combat.minHealth", 50)
Aurora.Config:Write("combat.maxRange", 40)

Setting Defaults
-- Set default values (used when no saved value exists)
Aurora.Config:SetDefault("myFeature.enabled", false)
Aurora.Config:SetDefault("combat.minHealth", 60)

tip
Always set defaults for your configuration values to ensure your addon works correctly even before the user changes any settings.

Setting Defaults
Always set defaults for your configuration values:

-- Set defaults when initializing your addon
Aurora.Config:SetDefault("combat.autoTarget", true)
Aurora.Config:SetDefault("combat.minHealth", 50)
Aurora.Config:SetDefault("ui.scale", 1.0)

tip
Setting defaults ensures your addon has fallback values if no user configuration exists.

Reading Configuration
-- Read with automatic default fallback
local autoTarget = Aurora.Config:Read("combat.autoTarget")
local minHealth = Aurora.Config:Read("combat.minHealth")

-- Get all settings
local allSettings = Aurora.Config:GetAll()
for key, value in pairs(allSettings) do
    print(key, value)
end

Writing Configuration
-- Write single values
Aurora.Config:Write("combat.autoTarget", false)
Aurora.Config:Write("ui.scale", 1.2)

-- Write multiple related settings
Aurora.Config:Write("spellQueue.enabled", true)
Aurora.Config:Write("spellQueue.window", 400)

Profile Integration
The configuration system automatically integrates with Aurora's profile system:

Character-Specific Settings
-- Saved as: configs/Aurora/AuroraGUISettings[CharacterName][ServerName].json


Named Profile Settings
-- Saved as: configs/Aurora/AuroraGUISettings[CharacterName][ServerName] - [ProfileName].json


Best Practices
Organize Keys Hierarchically
-- Good: Organized and clear
Aurora.Config:Write("healing.tanks.minHealth", 60)
Aurora.Config:Write("healing.raid.minHealth", 80)

-- Avoid: Flat and unclear
Aurora.Config:Write("tankMinHealth", 60)
Aurora.Config:Write("raidMinHealth", 80)

Set Defaults Early
local function InitializeDefaults()
    Aurora.Config:SetDefault("feature.enabled", false)
    Aurora.Config:SetDefault("feature.threshold", 50)
end

Use Consistent Keys
-- Define keys as constants
local CONFIG_KEYS = {
    ENABLED = "feature.enabled",
    THRESHOLD = "feature.threshold"
}

-- Use constants for consistency
Aurora.Config:Read(CONFIG_KEYS.ENABLED)
Aurora.Config:Write(CONFIG_KEYS.THRESHOLD, 75)

Handle Loading Errors


--

Enums
This section documents all the enumerations used in the Aurora Framework.

Class and Specialization
Class Enum
Represents the available classes in World of Warcraft.

Aurora.Enums.Class = {
    DEATHKNIGHT = 1,
    DEMONHUNTER = 2,
    DRUID = 3,
    HUNTER = 4,
    MAGE = 5,
    MONK = 6,
    PALADIN = 7,
    PRIEST = 8,
    ROGUE = 9,
    SHAMAN = 10,
    WARLOCK = 11,
    WARRIOR = 12,
    EVOKER = 13
}

Spec Enum
Represents all available specializations for each class.

Click to view all specializations
Role Detection
The framework provides helper functions to detect roles:

Aurora.Enums.IsHealer(specID): Returns true if the spec is a healer
Aurora.Enums.IsTank(specID): Returns true if the spec is a tank
Power Types
Represents different types of power resources used by classes.

Aurora.Enums.PowerTypes = {
    ["mana"] = 0,
    ["rage"] = 1,
    ["focus"] = 2,
    ["energy"] = 3,
    ["combopoints"] = 4,
    ["cp"] = 4,
    ["runes"] = 5,
    ["runicpower"] = 6,
    ["soulshards"] = 7,
    ["shards"] = 7,
    ["astralpower"] = 8,
    ["ap"] = 8,
    ["lunarpower"] = 8,
    ["holypower"] = 9,
    ["alternatepower"] = 10,
    ["maelstrom"] = 11,
    ["chi"] = 12,
    ["insanity"] = 13,
    ["arcanecharges"] = 16,
    ["fury"] = 17,
    ["pain"] = 18,
    ["essence"] = 19
}

Equipment
Item Classes
Main categories for items in the game.

Click to view all item classes
Aurora.Enums.ItemClass = {
    Consumable = 0,
    Container = 1,
    Weapon = 2,
    Gem = 3,
    Armor = 4,
    Reagent = 5,
    Projectile = 6,
    Tradegoods = 7,
    ItemEnhancement = 8,
    Recipe = 9,
    CurrencyTokenObsolete = 10,
    Quiver = 11,
    Questitem = 12,
    Key = 13,
    PermanentObsolete = 14,
    Miscellaneous = 15,
    Glyph = 16,
    Battlepet = 17,
    WoWToken = 18,
    Profession = 19

Weapon Subclasses
Specific types of weapons.

Click to view all weapon subclasses
Aurora.Enums.ItemWeaponSubclass = {
    Axe1H = 0,
    Axe2H = 1,
    Bows = 2,
    Guns = 3,
    Mace1H = 4,
    Mace2H = 5,
    Polearm = 6,
    Sword1H = 7,
    Sword2H = 8,
    Warglaive = 9,
    Staff = 10,
    Bearclaw = 11,
    Catclaw = 12,
    Unarmed = 13,
    Generic = 14,
    Dagger = 15,
    Thrown = 16,
    Obsolete3 = 17,
    Crossbow = 18,
    Wand = 19,
    Fishingpole = 20
}

Armor Subclasses
Types of armor items.

Aurora.Enums.ItemArmorSubclass = {
    Generic = 0,
    Cloth = 1,
    Leather = 2,
    Mail = 3,
    Plate = 4,
    Cosmetic = 5,
    Shield = 6,
    Libram = 7,
    Idol = 8,
    Totem = 9,
    Sigil = 10,
    Relic = 11
}

Armor Subclasses
Types of armor items.

Aurora.Enums.ItemArmorSubclass = {
    Generic = 0,
    Cloth = 1,
    Leather = 2,
    Mail = 3,
    Plate = 4,
    Cosmetic = 5,
    Shield = 6,
    Libram = 7,
    Idol = 8,
    Totem = 9,
    Sigil = 10,
    Relic = 11
}

Inventory Slots
Represents equipment slots where items can be equipped.

all inventory slots
Aurora.Enums.InvSlotName = {
    Ammo = 0,
    Head = 1,
    Neck = 2,
    Shoulders = 3,
    Shirt = 4,
    Chest = 5,
    Waist = 6,
    Legs = 7,
    Feet = 8,
    Wrist = 9,
    Hands = 10,
    Finger1 = 11,
    Finger2 = 12,
    Trinket1 = 13,
    Trinket2 = 14,
    Back = 15,
    MainHand = 16,
    OffHand = 17,
    Ranged = 18,
    Tabard = 19,
    ProfessionTool1 = 20,
    ProfessionAccessory1_1 = 21,
    ProfessionAccessory1_2 = 22,
    ProfessionTool2 = 23,
    ProfessionAccessory2_1 = 24,
    ProfessionAccessory2_2 = 25,
    CookingTool = 26,
    CookingAccessory = 27,
    FishingRod = 28,
    FishingAccessory1 = 29,
    FishingAccessory2 = 30
}


--

Lists
This section documents all the predefined lists used in the Aurora Framework.

Spell Lists
Interrupt Spells
The framework maintains a list of spells that should be interrupted. These are stored in:

Aurora.Lists.DefaultInterruptSpells: Default list of interrupt spells
Aurora.Lists.InterruptSpells: Working list that can be modified at runtime
Dispel Spells
Similar to interrupt spells, the framework tracks dispellable spells:

Aurora.Lists.DefaultDispelSpells: Default list of dispel spells
Aurora.Lists.DispelSpells: Working list that can be modified at runtime
Both spell lists are saved to and loaded from configuration files:

configs/DispelSpells.json
Purge Spells
The framework maintains a list of purge spells. These are stored in:

Aurora.Lists.DefaultPurgeSpells: Default list of purge spells
Aurora.Lists.PurgeSpells: List of purge spells
Both spell lists are saved to and loaded from configuration files:

configs/PurgeSpells.json
Soothe Spells
The framework maintains a list of soothe spells. These are stored in:

Aurora.Lists.DefaultSootheSpells: Default list of soothe spells
Aurora.Lists.SootheSpells: List of soothe spells
Both soothe spell lists are saved to and loaded from configuration files:

configs/SootheSpells.json
Gathering Lists
Gathering Ores
The framework maintains a list of ores that can be gathered. These are stored in:

Aurora.Lists.Ores: List of ores that can be gathered
Gathering Herbs
Similar to ores, the framework maintains a list of herbs that can be gathered:

Aurora.Lists.Herbs: List of herbs that can be gathered

--
Hooks
Documentation for Aurora hooks and integrations

--
Boss Mods API Reference
This documentation covers the API available for developers who want to interact with Aurora's Boss Mods functionality, particularly for timer tracking and pull coordination.

Timer Management
Getting Timers
-- Get all active timers
local timers = Aurora.BossMod:getactivetimers()

-- Get a specific timer by text match
local timer = Aurora.BossMod:gettimer("timer text")

-- Get all timers matching text
local matchingTimers = Aurora.BossMod:gettimers("timer text")

-- Check if a specific timer exists
local exists = Aurora.BossMod:hastimer("timer text")

-- Get remaining time for a specific timer
local remaining = Aurora.BossMod:gettimerremaining("timer text")


Pull Timer Functions
-- Get current pull timer information
local pullTimer = Aurora.BossMod:getpulltimer()

-- Check if currently pulling
local isPulling = Aurora.BossMod:ispulling()

-- Get remaining time on pull timer
local remaining = Aurora.BossMod:getpulltimeremaining()

-- Get formatted pull string
local pullString = Aurora.BossMod:getpullstring() -- e.g. "Pulling in 5.1 seconds (BigWigs)"


Timer Data Structure
When getting timer information, the timer objects have the following structure:

local timer = {
    text = "Timer Text",           -- The display text of the timer
    duration = 30,                 -- Total duration in seconds
    expirationTime = 1234567890,   -- When the timer expires (GetTime())
    remaining = 15.5,              -- Time remaining in seconds
    type = "bar",                  -- Timer type
    source = "BigWigs",            -- Which boss mod created the timer
    key = "uniqueKey",            -- Unique identifier (if provided)
    mod = bwModule                -- Reference to boss mod module (BigWigs only)
}


Example Usage
-- Example: React to specific timer
function CheckImportantTimer()
    if Aurora.BossMod:hastimer("Important Ability") then
        local remaining = Aurora.BossMod:gettimerremaining("Important Ability")
        if remaining < 5 then
            -- Prepare for ability
            PrepareForAbility()
        end
    end
end

-- Example: Pull timer coordination
function CheckPullStatus()
    if Aurora.BossMod:ispulling() then
        local remaining = Aurora.BossMod:getpulltimeremaining()
        if remaining <= 3 then
            -- Do pre-pull ability
            CastPrePullAbility()
        end
    end
end

--
Keyboard Hook API Reference
This documentation covers the keyboard hook API available in Aurora, which allows modules to register and handle keyboard events outside of WoW's default input system.

Key Code Enumeration
Aurora provides a comprehensive enumeration of virtual key codes through the Aurora.HotkeyEnum table, which maps keyboard keys to their corresponding virtual key codes.

-- Example key codes
Aurora.HotkeyEnum.A       -- Virtual key code for 'A'
Aurora.HotkeyEnum.SHIFT   -- Virtual key code for left Shift
Aurora.HotkeyEnum.SPACE   -- Virtual key code for Space


Key Binding System
The Aurora.KeyBindingSystem provides methods for registering and handling keyboard shortcuts.

Registering Key Bindings
-- Register a key binding using WoW-style hotkey string
Aurora.KeyBindingSystem:RegisterWoWHotkey("SHIFT-A", function(isPressed)
    if isPressed then
        -- Handle key press
        print("Shift+A pressed")
    end
end)

-- Register using raw key codes
local keyCodes = {Aurora.HotkeyEnum.CONTROL, Aurora.HotkeyEnum.C}
Aurora.KeyBindingSystem:RegisterKeyBinding(keyCodes, function(isPressed)
    if isPressed then
        -- Handle Ctrl+C
        print("Control+C pressed")
    end
end)

-- Register using a hotkey string
Aurora.KeyBindingSystem:RegisterHotkeyString("ALT-F4", function(isPressed)
    if isPressed then
        -- Handle Alt+F4
        print("Alt+F4 pressed")
    end
end)


Unregistering Key Bindings
-- Unregister a WoW-style hotkey
Aurora.KeyBindingSystem:UnregisterHotkeyString("SHIFT-A")

-- Unregister using key codes
local keyCodes = {Aurora.HotkeyEnum.CONTROL, Aurora.HotkeyEnum.C}
Aurora.KeyBindingSystem:UnregisterKeyBinding(keyCodes)

-- Clear all key bindings
Aurora.KeyBindingSystem:ClearKeyBindings()


Working with Hotkey Strings
Aurora provides utilities for parsing and creating hotkey strings:

-- Parse a hotkey string into components
local hotkeyComponents = Aurora.HotkeyEnum:ParseHotkeyString("CTRL-SHIFT-A")
-- Result: { modifiers = {"CTRL", "SHIFT"}, key = "A" }

-- Create a hotkey string from components
local hotkeyString = Aurora.HotkeyEnum:CreateHotkeyString({"SHIFT", "ALT"}, "B")
-- Result: "SHIFT-ALT-B"

-- Convert between WoW key names and virtual key codes
local keyCode = Aurora.HotkeyEnum:FromWoWKey("A") -- Get key code for 'A'
local keyName = Aurora.HotkeyEnum:ToWoWKey(0x00)  -- Get name for key code (returns "A")

-- Convert a hotkey string to virtual key codes
local keyCodes = Aurora.HotkeyEnum:HotkeyStringToKeyCodes("SHIFT-A")

-- Convert virtual key codes to a hotkey string
local hotkeyString = Aurora.HotkeyEnum:KeyCodesToHotkeyString({0x38, 0x00}) -- "SHIFT-A"


Short Example
-- Read the hotkey binding from config
local binding = Aurora.Config:Read("my_ability_hotkey")

-- Register the binding with the KeyBindingSystem
if binding and binding ~= "" then
    Aurora.KeyBindingSystem:RegisterWoWHotkey(binding, function(isPressed)
        if isPressed then 
        print("My ability activated!")
        end
    end)
end

--
Encounter Manager API Reference
This documentation covers the Encounter Manager API available.

Overview
The Encounter Manager provides a framework for:

Automatically tracking encounter start/end events
Managing boss unit tracking
Handling encounter-specific timing
Executing custom callbacks during encounters
Regular pulse updates during encounters
Basic Usage
-- Register an encounter
Aurora.EncounterManager.Encounters = {
    [2816] = {
        name = "Kyrioss",
        timing = true,
        track_bosses = true,
        callback = function(encounter)
            print("Encounter started:", encounter.name)
        end,
        -- Pulse callback called every updateRate seconds
        pulse = function(encounter, deltaTime)

            for guid, unit in pairs(encounter.bossUnits) do
                if unit.exists then
                    local pos = unit.position
                    print(string.format("%s: HP: %.1f%%, Pos: %.1f, %.1f, %.1f, Casting: %s", 
                        unit.name,
                        unit.hp,
                        pos.x, pos.y, pos.z,
                        unit.casting and unit.casting or "None"
                    ))
                end
            end
            
            if encounter.elapsedTime >= 60 then
                print("One minute into the fight!")
            end
        end
    }
}



Encounter Registration
Each encounter is registered with a configuration table that defines its behavior:

{
    name = string,           -- Encounter name
    timing = boolean,        -- Enable timing tracking
    track_bosses = boolean,  -- Enable boss unit tracking
    callback = function,     -- Called when encounter starts
    pulse = function        -- Called periodically during encounter
}


Encounter Configuration Options
name: String identifier for the encounter
timing: When true, tracks elapsed time
track_bosses: When true, automatically tracks boss units
callback: Function called when encounter starts
pulse: Function called every update interval
Encounter Info Structure
The encounter info object provided to callbacks contains:

---@class EncounterInfo
{
    id = number,            -- Encounter ID
    name = string,          -- Encounter name
    difficulty = number,    -- Difficulty ID
    groupSize = number,     -- Group size
    startTime = number,     -- When encounter started
    elapsedTime = number,   -- Time since start
    bossUnits = table,      -- Table of boss Unit objects
    isActive = boolean,     -- Whether encounter is active
    lastPulse = number,     -- Last pulse time
    deltaTime = number      -- Time since last pulse
}

API Methods
Getting Encounter Information
-- Get current encounter info
local encounter = Aurora.EncounterManager:GetCurrentEncounter()

-- Get elapsed time of current encounter
local time = Aurora.EncounterManager:GetEncounterElapsedTime()

-- Get active boss units
local bosses = Aurora.EncounterManager:GetActiveBossUnits()


Debug Mode
The Encounter Manager includes a debug mode that can be enabled for troubleshooting:

-- Enable debug mode
Aurora.EncounterManager.debug = true

-- Disable debug mode
Aurora.EncounterManager.debug = false

Update Rate Configuration
You can adjust how frequently the pulse callback is called:

-- Set update rate to 0.5 seconds
Aurora.EncounterManager.updateRate = 0.5

--

Discord Webhook
The Discord webhook hook provides functionality to send rich embeds and messages to Discord channels through webhooks.

Basic Usage
local Discord = Aurora.Discord

-- Set your webhook URL
Discord:SetWebhookUrl("your-webhook-url")

-- Create a basic embed
local embed = Discord.DiscordEmbed.new()
    :SetTitle("Hello World")
    :SetDescription("This is a test embed")
    :SetColor(0xFF0000) -- Red color

-- Send the embed
Discord:SendEmbed(embed)

Available Classes
DiscordEmbed
The main class for creating Discord embeds. Supports method chaining for easy configuration.

local embed = Discord.DiscordEmbed.new()

Methods
SetTitle(title): Sets the embed title
SetDescription(description): Sets the embed description
SetUrl(url): Sets the embed URL
SetTimestamp(timestamp): Sets the embed timestamp
SetColor(color): Sets the embed color (in decimal format)
SetFooter(footer): Sets the embed footer (requires EmbedFooter object)
SetImage(image): Sets the embed image (requires EmbedImage object)
SetThumbnail(thumbnail): Sets the embed thumbnail (requires EmbedImage object)
SetAuthor(author): Sets the embed author (requires EmbedAuthor object)
AddField(field): Adds a field to the embed (requires EmbedField object)
EmbedFooter
Creates a footer for the embed.

local footer = Discord.EmbedFooter.new(text, icon_url, proxy_icon_url)


Parameters
text: Footer text
icon_url (optional): URL for footer icon
proxy_icon_url (optional): Proxied URL for footer icon
EmbedImage
Creates an image or thumbnail for the embed.

local image = Discord.EmbedImage.new(url, proxy_url, height, width)


Parameters
url: Image URL
proxy_url (optional): Proxied image URL
height (optional): Image height
width (optional): Image width
EmbedAuthor
Creates an author section for the embed.

local author = Discord.EmbedAuthor.new(name, url, icon_url, proxy_icon_url)


Parameters
name: Author name
url (optional): Author URL
icon_url (optional): Author icon URL
proxy_icon_url (optional): Proxied author icon URL
EmbedField
Creates a field for the embed.

local field = Discord.EmbedField.new(name, value, inline)

Parameters
name: Field name
value: Field value
inline (optional): Whether the field should be inline (default: false)
Complete Example
Here's a comprehensive example showing all features:

local Discord = Aurora.Discord

-- Set webhook URL
Discord:SetWebhookUrl("your-webhook-url")

-- Create a full embed
local embed = Discord.DiscordEmbed.new()
    :SetTitle("Hello World")
    :SetDescription("This is a complete embed example")
    :SetUrl("https://aurora-wow.wtf")
    :SetColor(0xFF0000)
    :SetFooter(
        Discord.EmbedFooter.new(
            "Footer Text",
            "https://example.com/footer-icon.png"
        )
    )
    :SetImage(
        Discord.EmbedImage.new(
            "https://example.com/image.png"
        )
    )
    :SetThumbnail(
        Discord.EmbedImage.new(
            "https://example.com/thumbnail.png"
        )
    )
    :SetAuthor(
        Discord.EmbedAuthor.new(
            "Author Name",
            "https://example.com",
            "https://example.com/author-icon.png"
        )
    )
    :AddField(
        Discord.EmbedField.new("Field 1", "Value 1", true)
    )
    :AddField(
        Discord.EmbedField.new("Field 2", "Value 2", true)
    )

-- Send the embed
Discord:SendEmbed(embed)

Error Handling
The Discord webhook implementation includes basic error handling:

If webhook URL is not set, it will throw an error
Failed JSON encoding will be logged
Failed HTTP requests will be logged with status code and response
Successful webhook sends will be confirmed in the log
Best Practices
Set Webhook URL First: Always set the webhook URL before attempting to send embeds
Color Values: Use decimal color values (e.g., 0xFF0000 for red)
Field Limits: Discord has limits on embed fields (max 25 fields)
Content Length: Keep content within Discord's limits (max 2000 characters for regular messages)
Image URLs: Use direct image URLs that end in image extensions

--
State Registrar
The State Registrar provides a robust system for tracking and managing state in your Aurora modules. It's particularly useful for tracking time-windowed events and maintaining state access.

Core Implementation
The state registrar consists of two main components:

StateExpression: The core class for managing individual states
StateManager: A global manager for all state expressions
Creating a State Expression
local myState = Aurora.StateExpression:New("my_state", 0)

The New method accepts:

name: Unique identifier for the state
default: Initial value (defaults to 0)
State Expression Properties
Each state expression contains:

{
    name = "string",        -- Unique identifier
    value = any,           -- Current state value
    lastUpdate = number,   -- Last update timestamp
    window = number       -- Time window in seconds (default: 5)
}


Core Methods
-- Register an event handler
myState:RegisterHandler("EVENT_NAME", function(self, now, ...)
    -- Handle the event
end)

-- Update state based on an event
myState:Update("EVENT_NAME", ...)

-- Set the time window
myState:SetWindow(10) -- 10 seconds


Accessing State Values
-- Using __call metamethod
local value = myState()

-- Direct access
local directValue = myState.value

Advanced Example: Damage Tracker
Here's a comprehensive example that demonstrates the power of the state registrar by implementing a damage tracking system:

local StateExpression = Aurora.StateExpression

-- Create damage tracking state
local damageTaken = StateExpression:New("damage_taken")
damageTaken.hits = {} -- Store individual hits

-- Cleanup function for managing the hit window
local function cleanupOldHits(self, now)
    local windowStart = now - self.window
    local removed = 0

    -- Remove old hits
    while self.hits[1] and self.hits[1].time < windowStart do
        table.remove(self.hits, 1)
        removed = removed + 1
    end
    
    -- Recalculate total
    local total = 0
    for _, hit in ipairs(self.hits) do
        total = total + (tonumber(hit.amount) or 0)
    end
    
    -- Update only if changed
    if total ~= self.value then
        self.value = total
    end
    
    return removed
end

-- Setup event handling
local f = CreateFrame("Frame")
f:RegisterEvent("UNIT_COMBAT")

-- Periodic cleanup
local timerFrame = CreateFrame("Frame")
timerFrame:SetScript("OnUpdate", function(self, elapsed)
    if #damageTaken.hits > 0 then
        cleanupOldHits(damageTaken, GetTime())
    end
end)

-- Event forwarding
f:SetScript("OnEvent", function(self, event, ...)
    damageTaken:Update(event, ...)
end)

-- Register damage handler
damageTaken:RegisterHandler("UNIT_COMBAT", function(self, now, unitTarget, event, flagText, amount, schoolMask)
    if unitTarget ~= "player" then return end

    -- Process damage amount and type
    local damageAmount = tonumber(amount) or 0
    local damageType = "Unknown"
    
    -- Map damage school types
    local schoolTypes = {
        [1] = "Physical",
        [2] = "Holy",
        [4] = "Fire",
        [8] = "Nature",
        [16] = "Frost",
        [32] = "Shadow",
        [64] = "Arcane"
    }
    damageType = schoolTypes[schoolMask] or "Unknown"
    
    -- Record hit details
    table.insert(self.hits, {
        time = now,
        amount = damageAmount,
        type = damageType,
        isCrit = flagText == "CRITICAL",
        isCrushing = flagText == "CRUSHING",
        isGlancing = flagText == "GLANCING"
    })
    
    cleanupOldHits(self, now)
end)

-- Register in global state
Aurora.state.damage_taken = damageTaken


Using the Damage Tracker
-- Get total damage in current window
local totalDamage = damageTaken()

-- Analyze recent hits
for _, hit in ipairs(damageTaken.hits) do
    if hit.isCrit then
        print(string.format("%s critical hit for %d!", 
            hit.type, hit.amount))
    end
end

-- Get damage by type
local function getDamageByType(type)
    local total = 0
    for _, hit in ipairs(damageTaken.hits) do
        if hit.type == type then
            total = total + hit.amount
        end
    end
    return total
end

local physicalDamage = getDamageByType("Physical")

