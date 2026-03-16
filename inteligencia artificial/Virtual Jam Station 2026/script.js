// ==========================================
// 1. CONFIGURACIÓN GLOBAL Y AUDIO
// ==========================================
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

// Desbloquear audio con el primer clic
document.addEventListener('click', () => {
    if (audioCtx.state === 'suspended') audioCtx.resume();
}, { once: true });

// ==========================================
// 2. LÓGICA DEL PIANO (4 OCTAVAS)
// ==========================================
const notesData = [
    { n: "C", f: [130.81, 261.63, 523.25, 1046.50] },
    { n: "C#", f: [138.59, 277.18, 554.37, 1108.73] },
    { n: "D", f: [146.83, 293.66, 587.33, 1174.66] },
    { n: "D#", f: [155.56, 311.13, 622.25, 1244.51] },
    { n: "E", f: [164.81, 329.63, 659.25, 1318.51] },
    { n: "F", f: [174.61, 349.23, 698.46, 1396.91] },
    { n: "F#", f: [185.00, 369.99, 739.99, 1479.98] },
    { n: "G", f: [196.00, 392.00, 783.99, 1567.98] },
    { n: "G#", f: [207.65, 415.30, 830.61, 1661.22] },
    { n: "A", f: [220.00, 440.00, 880.00, 1760.00] },
    { n: "A#", f: [233.08, 466.16, 932.33, 1864.66] },
    { n: "B", f: [246.94, 493.88, 987.77, 1975.53] }
];

const allPianoNotes = {}; 

function createPiano() {
    const keyboard = document.getElementById('piano-keyboard');
    if(!keyboard) return;
    
    keyboard.innerHTML = '';
    for (let oct = 0; oct < 4; oct++) {
        const octaveNum = oct + 3;
        notesData.forEach(note => {
            const key = document.createElement('div');
            const isBlack = note.n.includes('#');
            key.className = `key ${isBlack ? 'black' : 'white'}`;
            
            const noteName = `${note.n}${octaveNum}`;
            const freq = note.f[oct];
            allPianoNotes[noteName] = freq;

            key.dataset.note = noteName;
            if (!isBlack) key.innerHTML = `<span>${note.n}</span>`;

            key.onclick = () => playSound(freq, 'triangle', 1);
            keyboard.appendChild(key);
        });
    }
}

// ==========================================
// 3. LÓGICA DE LA GUITARRA (CORREGIDA)
// ==========================================
// Afinación Estándar: Mi, La, Re, Sol, Si, Mi
const guitarBase = [82.41, 110.00, 146.83, 196.00, 246.94, 329.63];

function createGuitarNotes() {
    const guitarGrid = document.getElementById('guitar-notes');
    if(!guitarGrid) return;

    guitarGrid.innerHTML = '';
    
    // 6 Cuerdas (De la 6ta a la 1ra visualmente de arriba a abajo)
    for (let string = 0; string < 6; string++) {
        // 6 Trastes (El 0 es al aire)
        for (let fret = 0; fret < 6; fret++) {
            const noteBtn = document.createElement('div');
            noteBtn.className = 'fret-note';
            
            // Frecuencia real: base de la cuerda * 2^(traste/12)
            const freq = guitarBase[string] * Math.pow(2, fret / 12);
            
            noteBtn.onclick = () => {
                playGuitarSound(freq);
                noteBtn.classList.add('active-note');
                setTimeout(() => noteBtn.classList.remove('active-note'), 200);
            };
            
            guitarGrid.appendChild(noteBtn);
        }
    }
}

// ==========================================
// 4. MOTORES DE SONIDO
// ==========================================

function playSound(freq, type, decay) {
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const now = audioCtx.currentTime;

    osc.type = type;
    osc.frequency.setValueAtTime(freq, now);
    gain.gain.setValueAtTime(0.3, now);
    gain.gain.exponentialRampToValueAtTime(0.01, now + decay);

    osc.connect(gain);
    gain.connect(audioCtx.destination);
    osc.start();
    osc.stop(now + decay + 0.1);
}

function playGuitarSound(freq) {
    const oscBody = audioCtx.createOscillator();
    const oscHarmonic = audioCtx.createOscillator();
    const gain = audioCtx.createGain();
    const filter = audioCtx.createBiquadFilter();
    const now = audioCtx.currentTime;

    oscBody.type = 'sawtooth';
    oscBody.frequency.setValueAtTime(freq, now);
    
    oscHarmonic.type = 'triangle';
    oscHarmonic.frequency.setValueAtTime(freq * 2, now);

    filter.type = 'lowpass';
    filter.frequency.setValueAtTime(1500, now);
    filter.Q.setValueAtTime(5, now);

    gain.gain.setValueAtTime(0, now);
    gain.gain.linearRampToValueAtTime(0.4, now + 0.01);
    gain.gain.exponentialRampToValueAtTime(0.01, now + 2);

    oscBody.connect(filter);
    oscHarmonic.connect(filter);
    filter.connect(gain);
    gain.connect(audioCtx.destination);

    oscBody.start();
    oscHarmonic.start();
    oscBody.stop(now + 2.1);
    oscHarmonic.stop(now + 2.1);
}

// ==========================================
// 5. SELECTOR DE ACORDES
// ==========================================
const chords = {
    // --- MAYORES ---
    'C': { piano: ['C4', 'E4', 'G4'], guitar: [[1, 3], [2, 2], [4, 1]] },
    'D': { piano: ['D4', 'F#4', 'A4'], guitar: [[2, 0], [3, 2], [4, 3], [5, 2]] },
    'E': { piano: ['E3', 'G#3', 'B3'], guitar: [[0, 0], [1, 2], [2, 2], [3, 1]] },
    'F': { piano: ['F3', 'A3', 'C4'], guitar: [[2, 3], [3, 2], [4, 1], [5, 1]] }, // Simplificado para 5 trastes
    'G': { piano: ['G3', 'B3', 'D4'], guitar: [[0, 3], [1, 2], [5, 3]] },
    'A': { piano: ['A3', 'C#4', 'E4'], guitar: [[2, 2], [3, 2], [4, 2]] },
    'B': { piano: ['B3', 'D#4', 'F#4'], guitar: [[1, 2], [2, 4], [3, 4], [4, 4]] },

    // --- MENORES ---
    'Cm': { piano: ['C4', 'D#4', 'G4'], guitar: [[1, 3], [2, 1], [3, 0], [4, 1]] },
    'Dm': { piano: ['D4', 'F4', 'A4'], guitar: [[2, 0], [3, 2], [4, 3], [5, 1]] },
    'Em': { piano: ['E3', 'G3', 'B3'], guitar: [[1, 2], [2, 2]] },
    'Fm': { piano: ['F3', 'G#3', 'C4'], guitar: [[2, 3], [3, 1], [4, 1], [5, 1]] },
    'Am': { piano: ['A3', 'C4', 'E4'], guitar: [[2, 2], [3, 2], [4, 1]] },
    'Bm': { piano: ['B3', 'D4', 'F#4'], guitar: [[1, 2], [2, 4], [3, 4], [4, 3]] }
};

function showChord(chordName) {
    clearHighlights();
    const chord = chords[chordName];

    chord.piano.forEach(note => {
        const el = document.querySelector(`[data-note="${note}"]`);
        if (el) el.classList.add('highlight');
    });

    const allFretNotes = document.querySelectorAll('.fret-note');
    chord.guitar.forEach(pos => {
        const index = (pos[0] * 6) + pos[1];
        if (allFretNotes[index]) allFretNotes[index].classList.add('highlight');
    });
}

function clearHighlights() {
    document.querySelectorAll('.highlight').forEach(el => el.classList.remove('highlight'));
}

// ==========================================
// 6. NAVEGACIÓN Y TECLADO
// ==========================================

function showInstrument(type) {
    document.getElementById('piano-section').style.display = type === 'piano' ? 'block' : 'none';
    document.getElementById('guitarra-section').style.display = type === 'guitarra' ? 'block' : 'none';
    
    document.getElementById('btn-piano').classList.toggle('active', type === 'piano');
    document.getElementById('btn-guitarra').classList.toggle('active', type === 'guitarra');
}

window.onload = () => {
    createPiano();
    createGuitarNotes();
};

// --- DICCIONARIO MAESTRO DE ACORDES (BIBLIOTECA) ---
const globalChords = {
    // MAYORES
    "C": { type: "maj", p: ["C4", "E4", "G4"], g: [[1, 3], [2, 2], [4, 1]], f: [261.6, 329.6, 392.0] },
    "D": { type: "maj", p: ["D4", "F#4", "A4"], g: [[2, 0], [3, 2], [4, 3], [5, 2]], f: [293.6, 370.0, 440.0] },
    "E": { type: "maj", p: ["E3", "G#3", "B3"], g: [[0, 0], [1, 2], [2, 2], [3, 1]], f: [164.8, 207.6, 246.9] },
    "F": { type: "maj", p: ["F3", "A3", "C4"], g: [[2, 3], [3, 2], [4, 1], [5, 1]], f: [174.6, 220.0, 261.6] },
    "G": { type: "maj", p: ["G3", "B3", "D4"], g: [[0, 3], [1, 2], [5, 3]], f: [196.0, 246.9, 293.6] },
    "A": { type: "maj", p: ["A3", "C#4", "E4"], g: [[2, 2], [3, 2], [4, 2]], f: [220.0, 277.2, 329.6] },
    "B": { type: "maj", p: ["B3", "D#4", "F#4"], g: [[1, 2], [2, 4], [3, 4], [4, 4]], f: [246.9, 311.1, 370.0] },
    // MENORES
    "Cm": { type: "min", p: ["C4", "D#4", "G4"], g: [[1, 3], [2, 1], [4, 1]], f: [261.6, 311.1, 392.0] },
    "Dm": { type: "min", p: ["D4", "F4", "A4"], g: [[2, 0], [3, 2], [4, 3], [5, 1]], f: [293.6, 349.2, 440.0] },
    "Em": { type: "min", p: ["E3", "G3", "B3"], g: [[1, 2], [2, 2]], f: [164.8, 196.0, 246.9] },
    "Am": { type: "min", p: ["A3", "C4", "E4"], g: [[2, 2], [3, 2], [4, 1]], f: [220.0, 261.6, 329.6] },
    "Bm": { type: "min", p: ["B3", "D4", "F#4"], g: [[1, 2], [2, 4], [3, 4], [4, 3]], f: [246.9, 293.6, 370.0] },
    // SOSTENIDOS / BEMOLES
    "C#": { type: "acc", p: ["C#4", "F4", "G#4"], g: [[1, 4], [2, 3], [3, 1]], f: [277.2, 349.2, 415.3] },
    "Eb": { type: "acc", p: ["D#4", "G4", "A#4"], g: [[1, 1], [2, 1], [3, 3], [4, 4]], f: [311.1, 392.0, 466.1] },
    "F#": { type: "acc", p: ["F#3", "A#3", "C#4"], g: [[0, 2], [1, 4], [2, 4], [3, 3]], f: [185.0, 233.1, 277.2] },
    "Ab": { type: "acc", p: ["G#3", "C4", "D#4"], g: [[0, 4], [1, 6], [2, 6], [3, 5]], f: [207.6, 261.6, 311.1] },
    "Bb": { type: "acc", p: ["A#3", "D4", "F4"], g: [[1, 1], [2, 3], [3, 3], [4, 3]], f: [233.1, 293.6, 349.2] }
};

function initLibrary() {
    const lists = { maj: document.getElementById('list-maj'), min: document.getElementById('list-min'), acc: document.getElementById('list-acc') };
    
    Object.keys(globalChords).forEach(key => {
        const btn = document.createElement('button');
        btn.innerText = key;
        btn.onclick = () => selectLibraryChord(key);
        if(lists[globalChords[key].type]) lists[globalChords[key].type].appendChild(btn);
    });
}

function selectLibraryChord(key) {
    const chord = globalChords[key];
    document.getElementById('view-chord-title').innerText = "Acorde: " + key;
    
    // Sonido real del acorde (las 3 notas al tiempo)
    chord.f.forEach(freq => playSound(freq, 'triangle', 2));
    
    // Feedback visual en instrumentos
    // Usamos la función showChord que ya teníamos para iluminar piano y guitarra
    showChordFromLibrary(key);

    // Actualizar "Placeholders" (Simulación de fotos)
    document.getElementById('guitar-placeholder').innerText = `Diagrama: Cuerdas ${chord.g.map(pos => pos[0]+1).join(', ')} en trastes ${chord.g.map(pos => pos[1]).join(', ')}`;
    document.getElementById('piano-placeholder').innerText = `Notas: ${chord.p.join(' + ')}`;
}

// Función puente para iluminar
function showChordFromLibrary(name) {
    clearHighlights();
    const chord = globalChords[name];
    chord.p.forEach(note => {
        const el = document.querySelector(`[data-note="${note}"]`);
        if (el) el.classList.add('highlight');
    });
    const allFretNotes = document.querySelectorAll('.fret-note');
    chord.g.forEach(pos => {
        const index = (pos[0] * 6) + pos[1];
        if (allFretNotes[index]) allFretNotes[index].classList.add('highlight');
    });
}

// No olvides llamar a initLibrary() en window.onload

// Modificar showInstrument para que incluya la biblioteca
function showInstrument(type) {
    document.getElementById('piano-section').style.display = type === 'piano' ? 'block' : 'none';
    document.getElementById('guitarra-section').style.display = type === 'guitarra' ? 'block' : 'none';
    document.getElementById('biblioteca-section').style.display = type === 'biblioteca' ? 'block' : 'none';
    
    // Actualizar estados de botones
    document.querySelectorAll('.instrument-selector button').forEach(b => b.classList.remove('active'));
    document.getElementById('btn-' + type).classList.add('active');
}

window.onload = () => {
    createPiano();
    createGuitarNotes();
    initLibrary(); // Nueva función
};