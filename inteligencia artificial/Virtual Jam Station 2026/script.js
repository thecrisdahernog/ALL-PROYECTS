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

const allPianoNotes = {}; // Para el teclado físico

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
// 3. LÓGICA DE LA GUITARRA (TRASTES Y REALISMO)
// ==========================================
const guitarBase = [82.41, 110.00, 146.83, 196.00, 246.94, 329.63];

function createGuitarNotes() {
    const guitarGrid = document.getElementById('guitar-notes');
    if(!guitarGrid) return;

    guitarGrid.innerHTML = '';
    // 6 Cuerdas
    for (let string = 0; string < 6; string++) {
        // 6 Trastes (0 al 5)
        for (let fret = 0; fret < 6; fret++) {
            const noteBtn = document.createElement('div');
            noteBtn.className = 'fret-note';
            
            // Frecuencia: base de la cuerda * 2^(traste/12)
            const freq = guitarBase[5 - string] * Math.pow(2, fret / 12);
            
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

// Sonido para el Piano (Suave)
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

// Sonido para la Guitarra (Complejo/Realista)
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
// 5. NAVEGACIÓN Y TECLADO
// ==========================================

function showInstrument(type) {
    document.getElementById('piano-section').style.display = type === 'piano' ? 'block' : 'none';
    document.getElementById('guitarra-section').style.display = type === 'guitarra' ? 'block' : 'none';
    
    document.getElementById('btn-piano').classList.toggle('active', type === 'piano');
    document.getElementById('btn-guitarra').classList.toggle('active', type === 'guitarra');
}

// Teclado físico para la octava C4
const keyMap = { 'a': 'C4', 'w': 'C#4', 's': 'D4', 'e': 'D#4', 'd': 'E4', 'f': 'F4', 't': 'F#4', 'g': 'G4', 'y': 'G#4', 'h': 'A4', 'u': 'A#4', 'j': 'B4' };

window.addEventListener('keydown', (e) => {
    const noteName = keyMap[e.key.toLowerCase()];
    if (allPianoNotes[noteName]) {
        playSound(allPianoNotes[noteName], 'triangle', 1);
        const el = document.querySelector(`[data-note="${noteName}"]`);
        if (el) {
            el.classList.add('playing-css');
            setTimeout(() => el.classList.remove('playing-css'), 150);
        }
    }
});

// Inicialización general
window.onload = () => {
    createPiano();
    createGuitarNotes();
};