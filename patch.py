import re

file_path = r'C:\Users\leand\.gemini\antigravity\scratch\ficha_mm3e.html'
with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Update CSS
content = content.replace(':root {\n    --bg-body', ':root {\n    --gold: #FFD700; --comic-red: #CC2200;\n    --bg-body')

body_replacement = '''body {
  font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Arial,sans-serif;
  background:var(--bg-body);
  background-image: radial-gradient(circle, rgba(88,166,255,0.04) 1px, transparent 1px);
  background-size: 24px 24px;
  color:var(--text);
  line-height:1.55;
  font-size:15px;
}'''
content = re.sub(r'body\{[^\}]+\}', body_replacement, content)

comic_css = '''
.sidebar h2 {
  font-family: Impact, 'Arial Black', 'Arial Narrow', Arial, sans-serif;
  font-size: 1.6em;
  text-transform: uppercase;
  letter-spacing: 3px;
  color: var(--gold);
  text-shadow: 2px 2px 0 #000, -1px -1px 0 #000;
}

.hud-title {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: var(--gold);
}

.stat-title {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  letter-spacing: 2px;
  color: var(--gold);
}

.tab {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  padding:9px 13px;cursor:pointer;background:transparent;border:none;border-bottom:3px solid transparent;color:var(--muted);font-weight:700;font-size:.98em;transition:.15s;
}

.tab:hover{color:var(--text);}
.tab.active {
  color: var(--gold) !important;
  border-bottom-color: var(--gold) !important;
}

.btn-primary {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  background: var(--gold) !important;
  color: #000 !important;
  border:none!important;
}
.btn-primary:hover{background:var(--primary2)!important;}

.power-cost {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  color: var(--gold);
  font-size:1.2em;font-weight:700;
}

.tab-illustration {
  width: 100%;
  border-radius: 8px;
  overflow: hidden;
  margin-bottom: 16px;
  border: 3px solid var(--gold);
  box-shadow: 0 0 20px rgba(255,215,0,0.25), 0 0 40px rgba(88,166,255,0.1);
  max-height: 200px;
}

.tab-illustration img {
  width: 100%;
  height: 200px;
  object-fit: cover;
  object-position: center 30%;
  display: block;
}

.print-section-title {
  font-family: Impact, 'Arial Black', Arial, sans-serif;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: #000;
  font-size: 1.3em;
}
'''
content = content.replace('/* FORMS */', comic_css + '\n/* FORMS */')

# Delete some conflicting old css
content = re.sub(r'\.hud-title\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.tab\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.tab\.active\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.btn-primary\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.stat-title\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.power-cost\s*\{[^\}]+\}', '', content)
content = re.sub(r'\.print-section-title\s*\{[^\}]+\}', '', content)

# 2. Add hero banner
hero_banner = '''
<div style='width:100%;margin-bottom:18px;border-radius:10px;overflow:hidden;border:3px solid var(--gold);box-shadow:0 0 30px rgba(255,215,0,0.3);'>
  <img src='mm3e_banner.jpg' style='width:100%;height:160px;object-fit:cover;object-position:center 30%;display:block;' alt='M&M 3E Heroes'>
</div>
<!-- PRINT HEADER -->
'''
content = content.replace('<!-- PRINT HEADER -->', hero_banner)

# 3. Add drop down
old_select = '''<select id="archetypeSelect" onchange="loadArchetype(this.value)">
                <option value="">-- Criar do Zero --</option>
                <option value="invincible">Invencível (Mark Grayson)</option>
                <option value="omniman">Omni-Man (Nolan Grayson)</option>
                <option value="atomeve">Atom Eve (Samantha Wilkins)</option>
                <option value="rexsplode">Rex Splode</option>
                <option value="duplikate">Dupli-Kate</option>
                <option value="robot">Robot (Rudy)</option>
                <option value="techjacket">Tech Jacket</option>
            </select>'''
new_select = '''<select id="archetypeSelect" onchange="loadArchetype(this.value)">
                <option value="">-- Criar do Zero --</option>
                <optgroup label='── Invencível ──'>
                    <option value="invincible">Invencível (Mark Grayson)</option>
                    <option value="omniman">Omni-Man (Nolan Grayson)</option>
                    <option value="atomeve">Atom Eve (Samantha Wilkins)</option>
                    <option value="rexsplode">Rex Splode</option>
                    <option value="duplikate">Dupli-Kate</option>
                    <option value="robot">Robot (Rudy)</option>
                    <option value="techjacket">Tech Jacket</option>
                </optgroup>
                <optgroup label='── Invencível (Extras) ──'>
                  <option value='monster_girl'>Monster Girl</option>
                  <option value='black_samson'>Black Samson</option>
                  <option value='bulletproof'>Bulletproof</option>
                  <option value='battle_beast'>Battle Beast</option>
                  <option value='thragg'>Thragg (Vilão)</option>
                  <option value='conquest'>Conquest (Vilão)</option>
                  <option value='cecil'>Cecil Stedman</option>
                  <option value='darkwing'>Darkwing II</option>
                  <option value='shrinking_rae'>Shrinking Rae</option>
                  <option value='mauler_twin'>Mauler Twin</option>
                </optgroup>
                <optgroup label='── Marvel ──'>
                  <option value='spider_man'>Homem-Aranha</option>
                  <option value='iron_man'>Homem de Ferro</option>
                  <option value='captain_america'>Capitão América</option>
                  <option value='thor'>Thor</option>
                  <option value='hulk'>Hulk</option>
                  <option value='wolverine'>Wolverine</option>
                  <option value='storm'>Tempestade</option>
                  <option value='cyclops'>Ciclope</option>
                  <option value='magneto'>Magneto (Vilão)</option>
                  <option value='doctor_strange'>Doutor Estranho</option>
                  <option value='deadpool'>Deadpool</option>
                  <option value='black_panther'>Pantera Negra</option>
                </optgroup>
                <optgroup label='── DC ──'>
                  <option value='superman'>Superman</option>
                  <option value='batman'>Batman</option>
                  <option value='wonder_woman'>Mulher-Maravilha</option>
                  <option value='the_flash'>The Flash</option>
                  <option value='green_lantern'>Lanterna Verde</option>
                  <option value='aquaman'>Aquaman</option>
                  <option value='cyborg'>Ciborgue</option>
                  <option value='green_arrow'>Arqueiro Verde</option>
                  <option value='zatanna'>Zatanna</option>
                </optgroup>
            </select>'''
content = content.replace(old_select, new_select)

# 4. Ficha Tab Buttons & Content
tabs_html = '''<button class="tab" onclick="switchTab('tab-powers',this)">Poderes</button>
    <button class="tab" onclick="switchTab('tab-ficha',this)">📋 Ver Ficha</button>'''
content = content.replace('<button class="tab" onclick="switchTab(\'tab-powers\',this)">Poderes</button>', tabs_html)

ficha_div = '''<div id='tab-ficha' class='tab-content'>
  <div id='ficha-view'></div>
</div>

</main>'''
content = content.replace('</main>', ficha_div)

# 5. Illustrations
content = content.replace('<div id="tab-attr" class="tab-content print-section">\n    <div class="print-section-title" style="display:none;">Atributos</div>', '<div id="tab-attr" class="tab-content print-section">\n    <div class=\'tab-illustration\'><img src=\'mm3e_attr.jpg\' alt=\'Atributos\'></div>\n    <div class="print-section-title" style="display:none;">Atributos</div>')
content = content.replace('<div id="tab-powers" class="tab-content print-section">\n    <div class="print-section-title" style="display:none;">Poderes</div>', '<div id="tab-powers" class="tab-content print-section">\n    <div class=\'tab-illustration\'><img src=\'mm3e_powers.jpg\' alt=\'Poderes\'></div>\n    <div class="print-section-title" style="display:none;">Poderes</div>')
content = content.replace('<div id="tab-skills" class="tab-content print-section">\n    <div class="print-section-title" style="display:none;">Perícias</div>', '<div id="tab-skills" class="tab-content print-section">\n    <div class=\'tab-illustration\'><img src=\'mm3e_banner.jpg\' alt=\'\' style=\'object-position:left center;\'></div>\n    <div class="print-section-title" style="display:none;">Perícias</div>')
content = content.replace('<div id="tab-adv" class="tab-content print-section">\n    <div class="print-section-title" style="display:none;">Vantagens</div>', '<div id="tab-adv" class="tab-content print-section">\n    <div class=\'tab-illustration\'><img src=\'mm3e_banner.jpg\' alt=\'\' style=\'object-position:left center;\'></div>\n    <div class="print-section-title" style="display:none;">Vantagens</div>')


# 6. Add the new archetypes to the archetypes object
new_arch_data = '''
    // INVINCIBLE UNIVERSE ADDITIONS
    monster_girl: {
      np:10, characterName:'Monster Girl (Amanda)', identity:'Pública', player:'',
      attributes:{str:10,sta:10,agl:2,dex:2,fgt:8,int:2,awe:2,pre:2},
      defenses:{dodge:6,parry:2,fortitude:0,will:8,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:4},{id:'intimidation',name:'',ranks:6},{id:'expertise',name:'Magia',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'fearless',ranks:1},{id:'takedown',ranks:2}],
      powers:[
        {id:'p1',effectId:'growth',name:'Forma Monstruosa',ranks:4,modifiers:[]},
        {id:'p2',effectId:'regeneration',name:'Regeneração Acelerada',ranks:8,modifiers:[]},
        {id:'p3',effectId:'impervious_toughness',name:'Pele Espessa',ranks:8,modifiers:[]}
      ],
      complications:[{name:'Maldição',desc:'Fica mais velha a cada vez que usa o poder.'},{name:'Relacionamentos',desc:'Kirkman, equipe Guardians.'}]
    },
    black_samson: {
      np:10, characterName:'Black Samson', identity:'Pública', player:'',
      attributes:{str:8,sta:8,agl:2,dex:4,fgt:8,int:2,awe:2,pre:4},
      defenses:{dodge:6,parry:2,fortitude:2,will:6,toughness:0},
      skills:[{id:'intimidation',name:'',ranks:6},{id:'athletics',name:'',ranks:6},{id:'close_combat',name:'Desarmado',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'fearless',ranks:1},{id:'improved_initiative',ranks:1},{id:'takedown',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Raio de Energia',ranks:10,modifiers:[{modId:'ranged',ranks:10}]},
        {id:'p2',effectId:'protection',name:'Força Vital',ranks:8,modifiers:[]},
        {id:'p3',effectId:'flight',name:'Voo',ranks:6,modifiers:[]},
        {id:'p4',effectId:'immunity',name:'Suporte de Vida',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Motivação: Proteger os Fracos',desc:'Código de herói rígido.'},{name:'Rivalidade',desc:'Sempre em comparação com outros tijolos.'}]
    },
    bulletproof: {
      np:10, characterName:'Bulletproof (Zandale Randolph)', identity:'Secreta', player:'',
      attributes:{str:10,sta:10,agl:4,dex:2,fgt:8,int:1,awe:2,pre:2},
      defenses:{dodge:6,parry:2,fortitude:0,will:6,toughness:0},
      skills:[{id:'athletics',name:'',ranks:6},{id:'close_combat',name:'Desarmado',ranks:4},{id:'perception',name:'',ranks:4},{id:'persuasion',name:'',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'move_by_action',ranks:1},{id:'improved_initiative',ranks:1},{id:'interpose',ranks:1}],
      powers:[
        {id:'p1',effectId:'flight',name:'Voo Viltrumita',ranks:8,modifiers:[]},
        {id:'p2',effectId:'impervious_toughness',name:'Resistência Viltrumita',ranks:10,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Suporte de Vida',ranks:10,modifiers:[]}
      ],
      complications:[{name:'Motivação: Superar o pai',desc:'Vive à sombra de Invencível.'},{name:'Identidade Dupla',desc:'Vida universitária vs herói.'}]
    },
    battle_beast: {
      np:10, characterName:'Battle Beast', identity:'Pública', player:'',
      attributes:{str:14,sta:12,agl:2,dex:2,fgt:10,int:1,awe:2,pre:2},
      defenses:{dodge:4,parry:0,fortitude:0,will:4,toughness:0},
      skills:[{id:'intimidation',name:'',ranks:8},{id:'athletics',name:'',ranks:6},{id:'close_combat',name:'Machado de Guerra',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'fearless',ranks:1},{id:'improved_critical',ranks:2},{id:'extraordinary_effort',ranks:1}],
      powers:[
        {id:'p1',effectId:'impervious_toughness',name:'Pele de Pedra',ranks:12,modifiers:[]},
        {id:'p2',effectId:'immunity',name:'Suporte de Vida',ranks:10,modifiers:[]},
        {id:'p3',effectId:'regeneration',name:'Regeneração de Batalha',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Motivação: Glória em Combate',desc:'Só vive para lutar contra oponentes dignos.'},{name:'Berserker',desc:'Não para até o inimigo estar morto.'}]
    },
    thragg: {
      np:10, characterName:'Thragg (Vilão)', identity:'Pública', player:'',
      attributes:{str:12,sta:12,agl:2,dex:2,fgt:10,int:4,awe:2,pre:4},
      defenses:{dodge:2,parry:0,fortitude:0,will:4,toughness:0},
      skills:[{id:'intimidation',name:'',ranks:8},{id:'expertise',name:'Táticas Viltrumitas',ranks:8}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'takedown',ranks:2},{id:'fearless',ranks:1},{id:'assessment',ranks:1},{id:'extraordinary_effort',ranks:1}],
      powers:[
        {id:'p1',effectId:'flight',name:'Voo Viltrumita Superior',ranks:12,modifiers:[]},
        {id:'p2',effectId:'immunity',name:'Fisiologia Viltrumita',ranks:10,modifiers:[]}
      ],
      complications:[{name:'Motivação: Domínio Viltrumita',desc:'Construir um novo Império.'},{name:'Crueldade',desc:'Não tem misericórdia, mesmo com os seus.'}]
    },
    conquest: {
      np:10, characterName:'Conquest (Vilão)', identity:'Pública', player:'',
      attributes:{str:12,sta:12,agl:2,dex:2,fgt:10,int:2,awe:2,pre:2},
      defenses:{dodge:4,parry:0,fortitude:0,will:6,toughness:0},
      skills:[{id:'intimidation',name:'',ranks:8},{id:'close_combat',name:'Desarmado',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'takedown',ranks:2},{id:'fearless',ranks:1},{id:'improved_critical',ranks:1}],
      powers:[
        {id:'p1',effectId:'flight',name:'Voo Viltrumita',ranks:10,modifiers:[]},
        {id:'p2',effectId:'immunity',name:'Fisiologia Viltrumita',ranks:10,modifiers:[]},
        {id:'p3',effectId:'impervious_toughness',name:'Veterano de Guerras',ranks:10,modifiers:[]}
      ],
      complications:[{name:'Braço Prostético',desc:'Perdeu o braço para Invencível — ódio profundo.'},{name:'Motivação: Conquista',desc:'Subjugar planetas para o Império.'}]
    },
    cecil: {
      np:10, characterName:'Cecil Stedman', identity:'Secreta', player:'',
      attributes:{str:1,sta:2,agl:2,dex:4,fgt:4,int:10,awe:6,pre:6},
      defenses:{dodge:6,parry:6,fortitude:6,will:4,toughness:0},
      skills:[{id:'investigation',name:'',ranks:10},{id:'deception',name:'',ranks:10},{id:'intimidation',name:'',ranks:8},{id:'persuasion',name:'',ranks:6},{id:'technology',name:'',ranks:8},{id:'expertise',name:'Espionagem',ranks:10}],
      advantages:[{id:'assessment',ranks:1},{id:'eidetic_memory',ranks:1},{id:'benefit',ranks:3},{id:'equipment',ranks:4}],
      powers:[
        {id:'p1',effectId:'teleport',name:'Teletransporte Pessoal de Cecil',ranks:8,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p2',effectId:'immunity',name:'Implantes de Sobrevivência',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Motivação: Segurança da Terra',desc:'Faz o que for necessário.'},{name:'Agente Duplo',desc:'Suas lealdades são sempre questionáveis.'}]
    },
    darkwing: {
      np:10, characterName:'Darkwing II', identity:'Secreta', player:'',
      attributes:{str:2,sta:3,agl:8,dex:6,fgt:8,int:4,awe:4,pre:2},
      defenses:{dodge:4,parry:2,fortitude:5,will:6,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:8},{id:'stealth',name:'',ranks:10},{id:'investigation',name:'',ranks:6},{id:'close_combat',name:'Artes Marciais',ranks:4},{id:'intimidation',name:'',ranks:8}],
      advantages:[{id:'equipment',ranks:4},{id:'improved_initiative',ranks:1},{id:'move_by_action',ranks:1},{id:'uncanny_dodge',ranks:1},{id:'evasion',ranks:2},{id:'improved_critical',ranks:1}],
      powers:[
        {id:'p1',effectId:'concealment',name:'Camuflagem nas Sombras',ranks:4,modifiers:[]},
        {id:'p2',effectId:'senses',name:'Visão Noturna',ranks:2,modifiers:[]},
        {id:'p3',effectId:'movement',name:'Planar pelas sombras',ranks:4,modifiers:[{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Sombrio',desc:'Violento, cruza linhas que outros heróis não cruzariam.'},{name:'Identidade',desc:'Sucessor do Darkwing original — grandes expectativas.'}]
    },
    shrinking_rae: {
      np:10, characterName:'Shrinking Rae', identity:'Pública', player:'',
      attributes:{str:0,sta:2,agl:8,dex:8,fgt:4,int:2,awe:4,pre:3},
      defenses:{dodge:6,parry:6,fortitude:6,will:6,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:10},{id:'stealth',name:'',ranks:10},{id:'perception',name:'',ranks:6},{id:'athletics',name:'',ranks:4}],
      advantages:[{id:'evasion',ranks:2},{id:'improved_initiative',ranks:2},{id:'move_by_action',ranks:1},{id:'uncanny_dodge',ranks:1}],
      powers:[
        {id:'p1',effectId:'shrinking',name:'Miniaturização',ranks:8,modifiers:[{modId:'continuous',ranks:8}]},
        {id:'p2',effectId:'flight',name:'Asas Diminutas',ranks:4,modifiers:[]},
        {id:'p3',effectId:'damage',name:'Tiro de Energia Concentrado',ranks:6,modifiers:[{modId:'ranged',ranks:6}]}
      ],
      complications:[{name:'Tamanho Reduzido',desc:'Vulnerável a ser pisoteada ou não ser vista.'},{name:'Relacionamentos',desc:'Equipe de heróis, familia.'}]
    },
    mauler_twin: {
      np:10, characterName:'Mauler Twin', identity:'Pública', player:'',
      attributes:{str:12,sta:10,agl:2,dex:2,fgt:8,int:6,awe:2,pre:2},
      defenses:{dodge:4,parry:2,fortitude:0,will:4,toughness:0},
      skills:[{id:'technology',name:'',ranks:10},{id:'expertise',name:'Genética de Clones',ranks:10},{id:'close_combat',name:'Desarmado',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'eidetic_memory',ranks:1}],
      powers:[
        {id:'p1',effectId:'impervious_toughness',name:'Pele de Aço',ranks:10,modifiers:[]},
        {id:'p2',effectId:'protection',name:'Força Bruta',ranks:8,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Resistência Genética',ranks:5,modifiers:[]},
        {id:'p4',effectId:'leaping',name:'Salto Ampliado',ranks:4,modifiers:[]}
      ],
      complications:[{name:'Clone',desc:'Eles mesmos debatem qual é o original.'},{name:'Criminoso Habitual',desc:'Fichados e conhecidos pelas autoridades.'}]
    },
    spider_man: {
      np:10, characterName:'Homem-Aranha (Peter Parker)', identity:'Secreta', player:'',
      attributes:{str:5,sta:5,agl:10,dex:4,fgt:8,int:5,awe:6,pre:2},
      defenses:{dodge:0,parry:0,fortitude:3,will:4,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:6},{id:'athletics',name:'',ranks:4},{id:'stealth',name:'',ranks:4},{id:'perception',name:'',ranks:4},{id:'technology',name:'',ranks:6},{id:'expertise',name:'Ciência',ranks:6}],
      advantages:[{id:'evasion',ranks:2},{id:'uncanny_dodge',ranks:1},{id:'move_by_action',ranks:1},{id:'improved_initiative',ranks:1}],
      powers:[
        {id:'p1',effectId:'senses',name:'Sentido de Aranha',ranks:3,modifiers:[]},
        {id:'p2',effectId:'affliction',name:'Teia (Preso)',ranks:8,modifiers:[{modId:'ranged',ranks:8}]},
        {id:'p3',effectId:'movement',name:'Escalar Paredes',ranks:2,modifiers:[]},
        {id:'p4',effectId:'protection',name:'Traje Resistente',ranks:5,modifiers:[{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Identidade Secreta',desc:'Proteger tia May e MJ.'},{name:'Responsabilidade',desc:'Grande poder exige grande responsabilidade.'}]
    },
    iron_man: {
      np:10, characterName:'Homem de Ferro (Tony Stark)', identity:'Pública', player:'',
      attributes:{str:0,sta:2,agl:2,dex:4,fgt:4,int:10,awe:4,pre:6},
      defenses:{dodge:4,parry:4,fortitude:6,will:6,toughness:0},
      skills:[{id:'technology',name:'',ranks:10},{id:'expertise',name:'Engenharia',ranks:10},{id:'persuasion',name:'',ranks:8},{id:'investigation',name:'',ranks:6}],
      advantages:[{id:'eidetic_memory',ranks:1},{id:'assessment',ranks:1},{id:'benefit',ranks:3},{id:'equipment',ranks:2}],
      powers:[
        {id:'p1',effectId:'protection',name:'Armadura Stark',ranks:10,modifiers:[{modId:'impervious',ranks:10},{modId:'removable',ranks:1}]},
        {id:'p2',effectId:'damage',name:'Repulsores',ranks:10,modifiers:[{modId:'ranged',ranks:10},{modId:'removable',ranks:1}]},
        {id:'p3',effectId:'flight',name:'Propulsores',ranks:8,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p4',effectId:'immunity',name:'Suporte de Vida da Armadura',ranks:10,modifiers:[{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Armadura Removível',desc:'A armadura pode ser hackeada ou roubada.'},{name:'Ego',desc:'Confiante ao extremo, frequentemente age sozinho.'}]
    },
    captain_america: {
      np:10, characterName:'Capitão América (Steve Rogers)', identity:'Pública', player:'',
      attributes:{str:4,sta:4,agl:6,dex:6,fgt:8,int:4,awe:4,pre:6},
      defenses:{dodge:4,parry:2,fortitude:4,will:6,toughness:0},
      skills:[{id:'athletics',name:'',ranks:8},{id:'acrobatics',name:'',ranks:6},{id:'insight',name:'',ranks:6},{id:'persuasion',name:'',ranks:6},{id:'close_combat',name:'Escudo/Desarmado',ranks:4}],
      advantages:[{id:'assessment',ranks:1},{id:'benefit',ranks:1},{id:'leadership',pt:'Liderança',en:'Leadership',ranks:1},{id:'move_by_action',ranks:1},{id:'uncanny_dodge',ranks:1},{id:'evasion',ranks:2},{id:'ranged_attack',ranks:2}],
      powers:[
        {id:'p1',effectId:'protection',name:'Super-Soldado',ranks:4,modifiers:[]},
        {id:'p2',effectId:'damage',name:'Golpe de Escudo',ranks:8,modifiers:[{modId:'ranged',ranks:8},{modId:'alternate_effect',ranks:1}]},
        {id:'p3',effectId:'immunity',name:'Super-Metabolismo',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Motivação: Liberdade e Justiça',desc:'Nunca compromete seus valores.'},{name:'Homem fora do Tempo',desc:'Vem dos anos 40, às vezes não entende o mundo moderno.'}]
    },
    thor: {
      np:10, characterName:'Thor Odinson', identity:'Pública', player:'',
      attributes:{str:12,sta:12,agl:2,dex:2,fgt:8,int:2,awe:4,pre:6},
      defenses:{dodge:4,parry:2,fortitude:0,will:6,toughness:0},
      skills:[{id:'intimidation',name:'',ranks:6},{id:'athletics',name:'',ranks:4},{id:'expertise',name:'Mitologia Nórdica',ranks:6}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'fearless',ranks:1},{id:'improved_critical',ranks:1},{id:'move_by_action',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Mjolnir',ranks:10,modifiers:[{modId:'ranged',ranks:10},{modId:'penetrating',ranks:1}]},
        {id:'p2',effectId:'flight',name:'Voar com Mjolnir',ranks:6,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Resistência Asgardiana',ranks:10,modifiers:[]}
      ],
      complications:[{name:'Código de Honra',desc:'Luta com honra, mesmo contra inimigos.'},{name:'Arrogância',desc:'Filho de Odin — confiante ao extremo.'}]
    },
    hulk: {
      np:10, characterName:'Hulk (Bruce Banner - Médio)', identity:'Pública', player:'',
      attributes:{str:14,sta:14,agl:1,dex:1,fgt:8,int:0,awe:2,pre:2},
      defenses:{dodge:2,parry:2,fortitude:0,will:4,toughness:0},
      skills:[{id:'athletics',name:'',ranks:6},{id:'intimidation',name:'',ranks:10},{id:'close_combat',name:'Desarmado',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'fearless',ranks:1},{id:'improved_critical',ranks:1},{id:'takedown',ranks:2}],
      powers:[
        {id:'p1',effectId:'leaping',name:'Salto de Hulk',ranks:8,modifiers:[]},
        {id:'p2',effectId:'impervious_toughness',name:'Pele Verde Invulnerável',ranks:14,modifiers:[]},
        {id:'p3',effectId:'regeneration',name:'Regeneração Hulk',ranks:8,modifiers:[]},
        {id:'p4',effectId:'immunity',name:'Resistência Gamma',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Raiva de Banner',desc:'Hulk fica mais forte à medida que fica com raiva.'},{name:'Identidade Dupla',desc:'Banner e Hulk frequentemente em conflito.'}]
    },
    wolverine: {
      np:10, characterName:'Wolverine (Logan/James Howlett)', identity:'Pública', player:'',
      attributes:{str:4,sta:6,agl:6,dex:4,fgt:10,int:2,awe:4,pre:2},
      defenses:{dodge:6,parry:2,fortitude:2,will:6,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:4},{id:'athletics',name:'',ranks:4},{id:'intimidation',name:'',ranks:8},{id:'stealth',name:'',ranks:6},{id:'close_combat',name:'Garras de Adamantium',ranks:4},{id:'expertise',name:'Sobrevivência',ranks:6}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'fearless',ranks:1},{id:'improved_initiative',ranks:1},{id:'takedown',ranks:2},{id:'uncanny_dodge',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Garras de Adamantium',ranks:6,modifiers:[{modId:'penetrating',ranks:1}]},
        {id:'p2',effectId:'regeneration',name:'Fator de Cura',ranks:10,modifiers:[]},
        {id:'p3',effectId:'impervious_toughness',name:'Esqueleto de Adamantium',ranks:8,modifiers:[]},
        {id:'p4',effectId:'immunity',name:'Resistência a Venenos/Doenças',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Berserker',desc:'Em situações extremas pode perder o controle.'},{name:'Passado',desc:'Memórias fragmentadas e manipuladas.'}]
    },
    storm: {
      np:10, characterName:'Tempestade (Ororo Munroe)', identity:'Pública', player:'',
      attributes:{str:1,sta:2,agl:4,dex:4,fgt:4,int:3,awe:6,pre:8},
      defenses:{dodge:6,parry:6,fortitude:6,will:4,toughness:0},
      skills:[{id:'ranged_combat',name:'Poderes Climáticos',ranks:4},{id:'persuasion',name:'',ranks:8},{id:'expertise',name:'Meteorologia',ranks:8},{id:'acrobatics',name:'',ranks:4}],
      advantages:[{id:'attractive',ranks:1},{id:'assessment',ranks:1},{id:'fearless',ranks:1},{id:'move_by_action',ranks:1},{id:'precise_attack',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Raio',ranks:10,modifiers:[{modId:'ranged',ranks:10},{modId:'area',ranks:10}]},
        {id:'p2',effectId:'flight',name:'Controle do Vento',ranks:6,modifiers:[]},
        {id:'p3',effectId:'environment',name:'Tempestade',ranks:4,modifiers:[]},
        {id:'p4',effectId:'immunity',name:'Imunidade Climática',ranks:2,modifiers:[]}
      ],
      complications:[{name:'Claustrofobia',desc:'Em espaços fechados perde acesso total aos poderes.'},{name:'Motivação: Liberdade dos Mutantes',desc:'Luta pelos direitos mutantes.'}]
    },
    cyclops: {
      np:10, characterName:'Ciclope (Scott Summers)', identity:'Pública', player:'',
      attributes:{str:3,sta:3,agl:4,dex:6,fgt:6,int:4,awe:4,pre:4},
      defenses:{dodge:6,parry:4,fortitude:5,will:6,toughness:0},
      skills:[{id:'ranged_combat',name:'Raio Óptico',ranks:8},{id:'persuasion',name:'',ranks:6},{id:'insight',name:'',ranks:6},{id:'expertise',name:'Táticas',ranks:8}],
      advantages:[{id:'assessment',ranks:1},{id:'improved_critical',ranks:1},{id:'precise_attack',ranks:1},{id:'leadership',pt:'Liderança',en:'Leadership',ranks:1},{id:'benefit',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Raio Óptico',ranks:10,modifiers:[{modId:'ranged',ranks:10},{modId:'penetrating',ranks:1}]},
        {id:'p2',effectId:'protection',name:'Visor de Rubi',ranks:6,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p3',effectId:'immunity',name:'Imunidade ao próprio Raio',ranks:2,modifiers:[]}
      ],
      complications:[{name:'Óculos de Rubi',desc:'Sem o visor, não consegue controlar o poder — tudo se destrói.'},{name:'Liderança',desc:'O peso de liderar a equipe.'}]
    },
    magneto: {
      np:10, characterName:'Magneto (Erik Lehnsherr)', identity:'Pública', player:'',
      attributes:{str:1,sta:2,agl:2,dex:4,fgt:4,int:8,awe:6,pre:8},
      defenses:{dodge:6,parry:6,fortitude:6,will:4,toughness:0},
      skills:[{id:'ranged_combat',name:'Magnetismo',ranks:4},{id:'intimidation',name:'',ranks:10},{id:'persuasion',name:'',ranks:8},{id:'expertise',name:'Física do Magnetismo',ranks:10}],
      advantages:[{id:'assessment',ranks:1},{id:'fearless',ranks:1},{id:'benefit',ranks:2}],
      powers:[
        {id:'p1',effectId:'move_object',name:'Manipulação Magnética',ranks:10,modifiers:[{modId:'ranged',ranks:10}]},
        {id:'p2',effectId:'flight',name:'Campo Magnético Pessoal',ranks:6,modifiers:[]},
        {id:'p3',effectId:'protection',name:'Escudo Eletromagnético',ranks:8,modifiers:[{modId:'continuous',ranks:8}]},
        {id:'p4',effectId:'affliction',name:'Campo de Imobilização',ranks:6,modifiers:[{modId:'ranged',ranks:6},{modId:'area',ranks:6}]}
      ],
      complications:[{name:'Motivação: Supremacia Mutante',desc:'A humanidade ameaça os mutantes — deve agir primeiro.'},{name:'Holocausto',desc:'Sobrevivente do Holocausto — trauma profundo moldou a visão de mundo.'}]
    },
    doctor_strange: {
      np:10, characterName:'Doutor Estranho (Stephen Strange)', identity:'Pública', player:'',
      attributes:{str:1,sta:2,agl:2,dex:4,fgt:4,int:6,awe:8,pre:6},
      defenses:{dodge:6,parry:6,fortitude:6,will:2,toughness:0},
      skills:[{id:'expertise',name:'Artes Místicas',ranks:10},{id:'insight',name:'',ranks:6},{id:'persuasion',name:'',ranks:6},{id:'investigation',name:'',ranks:6}],
      advantages:[{id:'assessment',ranks:1},{id:'fearless',ranks:1},{id:'eidetic_memory',ranks:1},{id:'benefit',ranks:2}],
      powers:[
        {id:'p1',effectId:'damage',name:'Raios Místicos',ranks:10,modifiers:[{modId:'ranged',ranks:10}]},
        {id:'p2',effectId:'flight',name:'Capa Levitação',ranks:6,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p3',effectId:'create',name:'Construtos Místicos',ranks:6,modifiers:[]},
        {id:'p4',effectId:'nullify',name:'Supressão Mágica',ranks:6,modifiers:[{modId:'ranged',ranks:6}]},
        {id:'p5',effectId:'immunity',name:'Resistência Mística',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Mãos Danificadas',desc:'Tremor nas mãos — não pode mais realizar cirurgias.'},{name:'Responsabilidade',desc:'Único Feiticeiro Supremo da Terra.'}]
    },
    deadpool: {
      np:10, characterName:'Deadpool (Wade Wilson)', identity:'Pública', player:'',
      attributes:{str:3,sta:3,agl:8,dex:8,fgt:8,int:2,awe:2,pre:4},
      defenses:{dodge:4,parry:2,fortitude:5,will:4,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:6},{id:'close_combat',name:'Katanas/Desarmado',ranks:4},{id:'ranged_combat',name:'Pistolas',ranks:4},{id:'deception',name:'',ranks:8},{id:'intimidation',name:'',ranks:6},{id:'stealth',name:'',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'evasion',ranks:2},{id:'uncanny_dodge',ranks:1},{id:'move_by_action',ranks:1},{id:'improved_critical',ranks:2}],
      powers:[
        {id:'p1',effectId:'regeneration',name:'Fator de Cura Degenerado',ranks:10,modifiers:[]},
        {id:'p2',effectId:'immunity',name:'Imunidade ao Câncer/Doenças',ranks:5,modifiers:[]},
        {id:'p3',effectId:'damage',name:'Katanas de Vibranium',ranks:6,modifiers:[{modId:'penetrating',ranks:1}]},
        {id:'p4',effectId:'damage',name:'Pistolas',ranks:6,modifiers:[{modId:'ranged',ranks:6},{modId:'alternate_effect',ranks:1}]}
      ],
      complications:[{name:'Quarto Parede',desc:'Sabe que é personagem de quadrinho.'},{name:'Instabilidade Mental',desc:'Vozes na cabeça, humor imprevisível.'}]
    },
    black_panther: {
      np:10, characterName:"Pantera Negra (T'Challa)", identity:'Pública', player:'',
      attributes:{str:4,sta:4,agl:6,dex:6,fgt:8,int:8,awe:4,pre:6},
      defenses:{dodge:4,parry:2,fortitude:4,will:4,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:4},{id:'athletics',name:'',ranks:4},{id:'stealth',name:'',ranks:6},{id:'investigation',name:'',ranks:6},{id:'technology',name:'',ranks:8},{id:'expertise',name:'Vibranium',ranks:8}],
      advantages:[{id:'assessment',ranks:1},{id:'move_by_action',ranks:1},{id:'uncanny_dodge',ranks:1},{id:'equipment',ranks:2},{id:'benefit',ranks:2}],
      powers:[
        {id:'p1',effectId:'protection',name:'Traje de Vibranium',ranks:8,modifiers:[{modId:'impervious',ranks:8},{modId:'removable',ranks:1}]},
        {id:'p2',effectId:'senses',name:'Super-Sentidos da Erva',ranks:3,modifiers:[]},
        {id:'p3',effectId:'damage',name:'Garras de Vibranium',ranks:6,modifiers:[{modId:'penetrating',ranks:1},{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Rei de Wakanda',desc:'Responsabilidades reais que conflitam com ser herói.'},{name:'Orgulho',desc:'Relutante a pedir ajuda de outros.'}]
    },
    superman: {
      np:10, characterName:'Superman (Clark Kent)', identity:'Secreta', player:'',
      attributes:{str:14,sta:14,agl:2,dex:2,fgt:8,int:4,awe:4,pre:6},
      defenses:{dodge:4,parry:2,fortitude:0,will:6,toughness:0},
      skills:[{id:'athletics',name:'',ranks:4},{id:'persuasion',name:'',ranks:6},{id:'expertise',name:'Jornalismo',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'power_attack',ranks:1},{id:'interpose',ranks:1},{id:'move_by_action',ranks:1},{id:'fearless',ranks:1}],
      powers:[
        {id:'p1',effectId:'flight',name:'Voo Kryptoniano',ranks:10,modifiers:[]},
        {id:'p2',effectId:'impervious_toughness',name:'Invulnerabilidade',ranks:14,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Suporte de Vida',ranks:10,modifiers:[]},
        {id:'p4',effectId:'damage',name:'Visão de Calor',ranks:8,modifiers:[{modId:'ranged',ranks:8}]},
        {id:'p5',effectId:'senses',name:'Super Sentidos',ranks:5,modifiers:[]}
      ],
      complications:[{name:'Kryptonita',desc:'Vulnerabilidade fatal à kryptonita verde.'},{name:'Identidade Secreta',desc:'Proteger Martha Kent e os entes queridos.'}]
    },
    batman: {
      np:10, characterName:'Batman (Bruce Wayne)', identity:'Secreta', player:'',
      attributes:{str:4,sta:4,agl:6,dex:6,fgt:10,int:8,awe:4,pre:4},
      defenses:{dodge:4,parry:0,fortitude:4,will:6,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:6},{id:'athletics',name:'',ranks:4},{id:'investigation',name:'',ranks:10},{id:'stealth',name:'',ranks:6},{id:'intimidation',name:'',ranks:8},{id:'technology',name:'',ranks:6},{id:'expertise',name:'Criminologia',ranks:8},{id:'close_combat',name:'Artes Marciais',ranks:4}],
      advantages:[{id:'assessment',ranks:1},{id:'eidetic_memory',ranks:1},{id:'equipment',ranks:4},{id:'uncanny_dodge',ranks:1},{id:'improved_initiative',ranks:1},{id:'move_by_action',ranks:1},{id:'fearless',ranks:1},{id:'improved_critical',ranks:1}],
      powers:[
        {id:'p1',effectId:'senses',name:'Sentidos do Morcego',ranks:2,modifiers:[]},
        {id:'p2',effectId:'movement',name:'Garra/Planar',ranks:2,modifiers:[{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Sem Poderes',desc:'Apenas humano — equipamentos podem ser destruídos.'},{name:'Cruzada Pessoal',desc:'Os assassinatos dos pais. Nunca usa armas letais.'}]
    },
    wonder_woman: {
      np:10, characterName:'Mulher-Maravilha (Diana Prince)', identity:'Pública', player:'',
      attributes:{str:10,sta:10,agl:4,dex:4,fgt:10,int:4,awe:4,pre:6},
      defenses:{dodge:4,parry:0,fortitude:0,will:6,toughness:0},
      skills:[{id:'athletics',name:'',ranks:6},{id:'persuasion',name:'',ranks:6},{id:'expertise',name:'Mitologia Grega',ranks:6},{id:'insight',name:'',ranks:4}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'fearless',ranks:1},{id:'assessment',ranks:1},{id:'move_by_action',ranks:1},{id:'interpose',ranks:1}],
      powers:[
        {id:'p1',effectId:'flight',name:'Voo Divino',ranks:6,modifiers:[]},
        {id:'p2',effectId:'deflect',name:'Braceletes de Aegis',ranks:10,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Benção Divina',ranks:5,modifiers:[]},
        {id:'p4',effectId:'affliction',name:'Laço da Verdade',ranks:6,modifiers:[{modId:'ranged',ranks:6}]}
      ],
      complications:[{name:'Filha de Zeus',desc:'Responsabilidades olímpicas que interferem.'},{name:'Misericórdia',desc:'Prefere reformar a destruir inimigos.'}]
    },
    the_flash: {
      np:10, characterName:'The Flash (Barry Allen)', identity:'Secreta', player:'',
      attributes:{str:2,sta:4,agl:10,dex:4,fgt:4,int:4,awe:4,pre:2},
      defenses:{dodge:0,parry:6,fortitude:4,will:6,toughness:0},
      skills:[{id:'acrobatics',name:'',ranks:6},{id:'athletics',name:'',ranks:6},{id:'perception',name:'',ranks:6},{id:'expertise',name:'Química Forense',ranks:8}],
      advantages:[{id:'improved_initiative',ranks:4},{id:'evasion',ranks:2},{id:'move_by_action',ranks:1},{id:'uncanny_dodge',ranks:1},{id:'extraordinary_effort',ranks:1}],
      powers:[
        {id:'p1',effectId:'speed',name:'Força de Aceleração',ranks:14,modifiers:[]},
        {id:'p2',effectId:'quickness',name:'Velocidade de Processamento',ranks:8,modifiers:[]},
        {id:'p3',effectId:'damage',name:'Soco de Velocidade',ranks:6,modifiers:[{modId:'multiattack',ranks:6}]},
        {id:'p4',effectId:'immunity',name:'Fricção e Velocidade',ranks:3,modifiers:[]}
      ],
      complications:[{name:'Velocidade Viciante',desc:'Difícil desacelerar — ansiedade quando parado.'},{name:'Tragédia',desc:'Mãe morta, pai preso injustamente.'}]
    },
    green_lantern: {
      np:10, characterName:'Lanterna Verde (Hal Jordan)', identity:'Secreta', player:'',
      attributes:{str:2,sta:4,agl:4,dex:4,fgt:6,int:4,awe:4,pre:6},
      defenses:{dodge:6,parry:4,fortitude:4,will:6,toughness:0},
      skills:[{id:'ranged_combat',name:'Anel de Poder',ranks:4},{id:'vehicles',name:'',ranks:8},{id:'expertise',name:'Pilotagem de Combate',ranks:8},{id:'athletics',name:'',ranks:4}],
      advantages:[{id:'fearless',ranks:1},{id:'assessment',ranks:1},{id:'move_by_action',ranks:1},{id:'improved_initiative',ranks:1}],
      powers:[
        {id:'p1',effectId:'create',name:'Construtos de Luz Verde',ranks:10,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p2',effectId:'damage',name:'Rajada de Energia',ranks:10,modifiers:[{modId:'ranged',ranks:10},{modId:'removable',ranks:1}]},
        {id:'p3',effectId:'flight',name:'Voo do Anel',ranks:8,modifiers:[{modId:'removable',ranks:1}]},
        {id:'p4',effectId:'immunity',name:'Suporte de Vida do Anel',ranks:10,modifiers:[{modId:'removable',ranks:1}]}
      ],
      complications:[{name:'Poder Limitado pelo Anel',desc:'O anel precisa ser recarregado na lanterna a cada 24h.'},{name:'Fraqueza: Amarelo',desc:'Anel ineficaz contra objetos amarelos.'}]
    },
    aquaman: {
      np:10, characterName:'Aquaman (Arthur Curry)', identity:'Pública', player:'',
      attributes:{str:10,sta:10,agl:4,dex:4,fgt:8,int:4,awe:4,pre:6},
      defenses:{dodge:4,parry:2,fortitude:0,will:6,toughness:0},
      skills:[{id:'athletics',name:'',ranks:6},{id:'persuasion',name:'',ranks:6},{id:'expertise',name:'Oceanos e Criaturas Marinhas',ranks:8}],
      advantages:[{id:'all_out_attack',ranks:1},{id:'move_by_action',ranks:1},{id:'fearless',ranks:1},{id:'benefit',ranks:2}],
      powers:[
        {id:'p1',effectId:'swimming',name:'Natação Super-humana',ranks:10,modifiers:[]},
        {id:'p2',effectId:'communication',name:'Telepatia com Vida Marinha',ranks:2,modifiers:[]},
        {id:'p3',effectId:'immunity',name:'Pressão/Frio/Respirar Embaixo d\'água',ranks:8,modifiers:[]},
        {id:'p4',effectId:'impervious_toughness',name:'Pele para Pressão Oceânica',ranks:8,modifiers:[]}
      ],
      complications:[{name:'Fora d\'Água',desc:'Perde força e desidrata fora do ambiente aquático.'},{name:'Dois Mundos',desc:'Dividido entre Atlantis e a superfície.'}]
    },
    cyborg: {
      np:10, characterName:'Ciborgue (Victor Stone)', identity:'Pública', player:'',
      attributes:{str:8,sta:0,agl:2,dex:6,fgt:6,int:8,awe:4,pre:4},
      defenses:{dodge:6,parry:4,fortitude:10,will:6,toughness:0},
      skills:[{id:'technology',name:'',ranks:10},{id:'ranged_combat',name:'Canhão de Sônica',ranks:4},{id:'investigation',name:'',ranks:6},{id:'expertise',name:'Eletrônica',ranks:8}],
      advantages:[{id:'eidetic_memory',ranks:1},{id:'assessment',ranks:1},{id:'benefit',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Canhão de Plasma',ranks:10,modifiers:[{modId:'ranged',ranks:10}]},
        {id:'p2',effectId:'protection',name:'Exo-esqueleto de Titânio',ranks:10,modifiers:[{modId:'impervious',ranks:10}]},
        {id:'p3',effectId:'immunity',name:'Sistemas Cibernéticos',ranks:10,modifiers:[]},
        {id:'p4',effectId:'flight',name:'Propulsores',ranks:4,modifiers:[]}
      ],
      complications:[{name:'Corpo Cibernético',desc:'Percepcionado como máquina, não como humano.'},{name:'Conflito de Identidade',desc:'Quanto de si ainda é humano?'}]
    },
    green_arrow: {
      np:10, characterName:'Arqueiro Verde (Oliver Queen)', identity:'Secreta', player:'',
      attributes:{str:3,sta:3,agl:6,dex:10,fgt:6,int:4,awe:4,pre:4},
      defenses:{dodge:6,parry:4,fortitude:5,will:6,toughness:0},
      skills:[{id:'ranged_combat',name:'Arco e Flecha',ranks:8},{id:'acrobatics',name:'',ranks:6},{id:'stealth',name:'',ranks:6},{id:'athletics',name:'',ranks:6},{id:'insight',name:'',ranks:4}],
      advantages:[{id:'precise_attack',ranks:1},{id:'improved_critical',ranks:2},{id:'equipment',ranks:4},{id:'move_by_action',ranks:1},{id:'evasion',ranks:1},{id:'uncanny_dodge',ranks:1}],
      powers:[
        {id:'p1',effectId:'damage',name:'Flecha de Explosão',ranks:8,modifiers:[{modId:'ranged',ranks:8},{modId:'area',ranks:8},{modId:'removable',ranks:1}]},
        {id:'p2',effectId:'affliction',name:'Flecha de Paralisação',ranks:8,modifiers:[{modId:'ranged',ranks:8},{modId:'alternate_effect',ranks:1}]}
      ],
      complications:[{name:'Flecha Verde sem Poderes',desc:'Apenas habilidades, equipamento pode ser destruído.'},{name:'Política',desc:'Ideológico — conflitos com outros heróis.'}]
    },
    zatanna: {
      np:10, characterName:'Zatanna (Zatanna Zatara)', identity:'Pública', player:'',
      attributes:{str:1,sta:2,agl:4,dex:4,fgt:4,int:6,awe:8,pre:8},
      defenses:{dodge:6,parry:6,fortitude:6,will:2,toughness:0},
      skills:[{id:'persuasion',name:'',ranks:8},{id:'deception',name:'',ranks:4},{id:'expertise',name:'Artes Místicas',ranks:10},{id:'ranged_combat',name:'Magia',ranks:4}],
      advantages:[{id:'assessment',ranks:1},{id:'fearless',ranks:1},{id:'attractive',ranks:1},{id:'eidetic_memory',ranks:1}],
      powers:[
        {id:'p1',effectId:'affliction',name:'Magia de Controle',ranks:8,modifiers:[{modId:'ranged',ranks:8}]},
        {id:'p2',effectId:'transform',name:'Transmutação',ranks:6,modifiers:[{modId:'ranged',ranks:6}]},
        {id:'p3',effectId:'nullify',name:'Anti-Magia',ranks:6,modifiers:[{modId:'ranged',ranks:6}]},
        {id:'p4',effectId:'protection',name:'Escudo Mágico',ranks:6,modifiers:[]}
      ],
      complications:[{name:'Magia por Palavras',desc:'Precisa falar de trás para frente para usar magia — silêncio/mordaça a desativa.'},{name:'Responsabilidade',desc:'Guardiã de segredos ocultos do mundo.'}]
    }
'''

content = content.replace("        complications:[{name:'Dispositivo Preso',desc:'A armadura não pode ser removida.'}]}", "        complications:[{name:'Dispositivo Preso',desc:'A armadura não pode ser removida.'}]}," + new_arch_data)

# 7. Add renderFichaView JS and call it inside renderAll()
render_ficha = '''
function renderFichaView() {
  const el = document.getElementById('ficha-view');
  if (!el) return;
  const np = state.np;
  const costs = calcCosts();
  const total = costs.a + costs.d + costs.sk + costs.adv + costs.pw;
  const budget = np * 15;

  let toughTotal = getAttr('sta') + (state.defenses.toughness || 0);
  state.powers.forEach(p => { if (p.effectId === 'protection') toughTotal += p.ranks; });

  const dodge  = getAttr('agl') + (state.defenses.dodge || 0);
  const parry  = getAttr('fgt') + (state.defenses.parry || 0);
  const fort   = getAttr('sta') + (state.defenses.fortitude || 0);
  const will   = getAttr('awe') + (state.defenses.will || 0);
  const initAdv = state.advantages.find(a => a.id === 'improved_initiative');
  const initiative = getAttr('agl') + (initAdv ? initAdv.ranks * 4 : 0);
  const atk_melee = getAttr('fgt') + (state.skills.find(s => s.id === 'close_combat')?.ranks || 0);
  const atk_range = getAttr('dex') + (state.skills.find(s => s.id === 'ranged_combat')?.ranks || 0);

  const overBudget = total > budget;

  // Section helper
  const section = (title, content) => `
    <div style='margin-bottom:20px;'>
      <div style='font-family:Impact,Arial Black,Arial,sans-serif;font-size:1.1em;letter-spacing:2px;text-transform:uppercase;color:var(--gold);border-bottom:2px solid var(--gold);padding-bottom:4px;margin-bottom:10px;'>${title}</div>
      ${content}
    </div>`;

  // Combat stat box helper
  const statBox = (label, val, sub='') => `
    <div style='background:rgba(255,215,0,0.07);border:1px solid var(--gold);border-radius:6px;padding:8px 12px;text-align:center;min-width:80px;'>
      <div style='font-size:1.6em;font-weight:700;color:var(--primary);font-family:Impact,Arial Black,Arial,sans-serif;'>${val >= 0 ? (typeof val === 'number' ? (val > 0 ? '+' : '') + val : val) : val}</div>
      <div style='font-size:.75em;color:var(--gold);font-weight:700;text-transform:uppercase;letter-spacing:1px;'>${label}</div>
      ${sub ? `<div style='font-size:.7em;color:var(--muted);'>${sub}</div>` : ''}
    </div>`;

  // Attribute row helper
  const attrRow = (pt, en, id, note='') => {
    const val = getAttr(id);
    return `<div style='display:flex;justify-content:space-between;align-items:center;padding:5px 8px;border-bottom:1px solid rgba(255,255,255,0.05);'>
      <span style='font-weight:700;color:var(--accent);'>${pt}</span>
      <span style='font-size:.8em;color:var(--muted);'>${en}</span>
      <span style='font-size:1.2em;font-weight:700;color:var(--primary);min-width:30px;text-align:right;'>${val >= 0 ? '+' + val : val}</span>
    </div>`;
  };

  el.innerHTML = `
    <!-- HERO HEADER -->
    <div style='background:linear-gradient(135deg,rgba(255,215,0,0.08),rgba(88,166,255,0.05));border:2px solid var(--gold);border-radius:12px;padding:20px 24px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:12px;'>
      <div>
        <div style='font-family:Impact,Arial Black,Arial,sans-serif;font-size:2em;color:var(--gold);letter-spacing:2px;text-transform:uppercase;line-height:1;'>${state.characterName || 'Sem Nome'}</div>
        <div style='color:var(--muted);margin-top:4px;font-size:.9em;'>Identidade: <b style='color:var(--text);'>${state.identity || '—'}</b> &nbsp;|&nbsp; Jogador: <b style='color:var(--text);'>${state.player || '—'}</b></div>
      </div>
      <div style='text-align:right;'>
        <div style='font-size:.85em;color:var(--muted);'>Nível de Poder</div>
        <div style='font-size:2.5em;font-weight:700;color:var(--primary);line-height:1;'>NP ${np}</div>
        <div style='font-size:.85em;color:${overBudget ? 'var(--danger)' : 'var(--success)'};font-weight:700;'>${total} / ${budget} pts ${overBudget ? '⚠ ACIMA DO LIMITE' : '✓'}</div>
      </div>
    </div>

    ${section('Estatísticas de Combate',
      `<div style='display:flex;gap:10px;flex-wrap:wrap;'>
        ${statBox('Atq. Corpo', atk_melee, 'FGT+Perícia')}
        ${statBox('Atq. Dist.', atk_range, 'DEX+Perícia')}
        ${statBox('Esquiva', dodge, 'AGL+Comprado')}
        ${statBox('Aparar', parry, 'FGT+Comprado')}
        ${statBox('Resist.', toughTotal, 'STA+Proteção')}
        ${statBox('Fortitude', fort, 'STA+Comprado')}
        ${statBox('Vontade', will, 'AWE+Comprado')}
        ${statBox('Iniciativa', initiative >= 0 ? '+' + initiative : initiative, 'AGL+Vant.')}
      </div>`
    )}

    <div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;flex-wrap:wrap;'>
      ${section('Atributos',
        `<div style='background:rgba(0,0,0,.2);border-radius:8px;overflow:hidden;border:1px solid var(--border);'>
          ${dictAttrs.map(a => attrRow(a.pt, a.en, a.id)).join('')}
        </div>`
      )}

      ${section('Defesas',
        `<div style='background:rgba(0,0,0,.2);border-radius:8px;overflow:hidden;border:1px solid var(--border);'>
          ${dictDefenses.map(d => {
            const base = d.isToughness ? getAttr('sta') : getAttr(d.base);
            const bought = state.defenses[d.id] || 0;
            const tot = d.isToughness ? toughTotal : (base + bought);
            return `<div style='display:flex;justify-content:space-between;align-items:center;padding:5px 8px;border-bottom:1px solid rgba(255,255,255,0.05);'>
              <span style='font-weight:700;color:var(--accent);'>${d.pt}</span>
              <span style='font-size:.8em;color:var(--muted);'>${d.en}</span>
              <span style='font-size:1.2em;font-weight:700;color:var(--primary);'>${tot}</span>
            </div>`;
          }).join('')}
        </div>`
      )}
    </div>

    ${section('Poderes',
      state.powers.length === 0
        ? `<p style='color:var(--muted);font-style:italic;'>Nenhum poder registrado.</p>`
        : `<div style='display:flex;flex-direction:column;gap:6px;'>${state.powers.map(p => {
            const eff = dictEffects.find(e => e.id === p.effectId);
            const cost = calcPowerCost(p);
            const modNames = p.modifiers.map(m => { const md = dictModifiers.find(x => x.id === m.modId); return md ? md.pt : ''; }).filter(Boolean).join(', ');
            return `<div style='background:rgba(255,215,0,0.04);border:1px solid rgba(255,215,0,0.2);border-left:4px solid var(--gold);border-radius:0 6px 6px 0;padding:8px 12px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:6px;'>
              <div>
                <b style='color:var(--text);'>${p.name || 'Poder'}</b>
                <span style='font-size:.8em;color:var(--muted);margin-left:8px;'>[${eff ? eff.pt : p.effectId}] Rank ${p.ranks}${modNames ? ' · ' + modNames : ''}</span>
              </div>
              <span style='font-weight:700;color:var(--gold);font-family:Impact,Arial Black,Arial,sans-serif;'>${cost} pts</span>
            </div>`;
          }).join('')}</div>`
    )}

    <div style='display:grid;grid-template-columns:1fr 1fr;gap:20px;'>
      ${section('Vantagens',
        state.advantages.length === 0
          ? `<p style='color:var(--muted);font-style:italic;'>Nenhuma.</p>`
          : state.advantages.map(adv => {
              const def = dictAdvantages.find(d => d.id === adv.id);
              return `<div style='display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.05);font-size:.9em;'><span>${def ? def.pt : adv.id}</span><span style='color:var(--primary);'>${adv.ranks}${adv.ranks > 1 ? ' ranks' : ''}</span></div>`;
            }).join('')
      )}

      ${section('Perícias com Ranks',
        state.skills.filter(s => s.ranks > 0).length === 0
          ? `<p style='color:var(--muted);font-style:italic;'>Nenhuma.</p>`
          : state.skills.filter(s => s.ranks > 0).map(sk => {
              const def = dictSkills.find(d => d.id === sk.id) || { pt: sk.id, base: 'int' };
              const total = getAttr(def.base) + sk.ranks;
              return `<div style='display:flex;justify-content:space-between;padding:4px 0;border-bottom:1px solid rgba(255,255,255,.05);font-size:.9em;'><span>${def.pt}${sk.name ? ': ' + sk.name : ''}</span><span style='color:var(--primary);font-weight:700;'>+${total}</span></div>`;
            }).join('')
      )}
    </div>

    ${state.complications.length > 0 ? section('Complicações',
      `<ul style='list-style:none;padding:0;'>${state.complications.map(c =>
        `<li style='padding:5px 0;border-bottom:1px solid rgba(255,255,255,.05);font-size:.9em;'><b style='color:var(--gold);'>⚡ ${c.name || 'Complicação'}:</b> ${c.desc || ''}</li>`
      ).join('')}</ul>`
    ) : ''}
  `;
}
'''

content = content.replace('/* ===== RENDER ===== */', render_ficha + '\n/* ===== RENDER ===== */')

content = content.replace("    const spd=state.powers.find(p=>p.effectId==='flight'||p.effectId==='speed');\n    document.getElementById('hudSpeed').textContent=spd?(30*Math.pow(2,spd.ranks)*0.3).toFixed(0)+' m/turno':'9 m/turno';\n}", "    const spd=state.powers.find(p=>p.effectId==='flight'||p.effectId==='speed');\n    document.getElementById('hudSpeed').textContent=spd?(30*Math.pow(2,spd.ranks)*0.3).toFixed(0)+' m/turno':'9 m/turno';\n    renderFichaView();\n}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print('Basic HTML edits done.')
