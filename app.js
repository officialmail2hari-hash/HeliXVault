const input = document.getElementById('file');
const status = document.getElementById('status');

input.addEventListener('change', async () => {

    const f = input.files[0];

    if (!f) return;

    status.textContent = `✓ Reading ${f.name}...`;

    // Read file
    const buffer = await f.arrayBuffer();
    const bytes = new Uint8Array(buffer);

    // -----------------------------
    // 1. BINARY
    // -----------------------------

    let binary = '';

    for (const b of bytes) {
        binary += b.toString(2).padStart(8, '0');
    }

    // -----------------------------
    // 2. DNA ENCODING
    // -----------------------------

    const map = {
        "00": "A",
        "01": "C",
        "10": "G",
        "11": "T"
    };

    let dna = '';

    for (let i = 0; i < binary.length; i += 2) {
        dna += map[binary.slice(i, i + 2)];
    }

    // -----------------------------
    // 3. GC CONTENT
    // -----------------------------

    let gcCount = 0;

    for (const base of dna) {
        if (base === "G" || base === "C") {
            gcCount++;
        }
    }

    const gcContent =
        dna.length === 0
            ? 0
            : (gcCount / dna.length) * 100;

    // -----------------------------
    // 4. LONGEST HOMOPOLYMER
    // -----------------------------

    let longestHomopolymer = 0;
    let currentRun = 0;
    let previous = '';

    for (const base of dna) {

        if (base === previous) {
            currentRun++;
        } else {
            currentRun = 1;
            previous = base;
        }

        longestHomopolymer =
            Math.max(longestHomopolymer, currentRun);
    }

    // -----------------------------
    // 5. SHA-256
    // -----------------------------

    const hashBuffer =
        await crypto.subtle.digest("SHA-256", bytes);

    const hashArray =
        Array.from(new Uint8Array(hashBuffer));

    const sha256 =
        hashArray
            .map(b => b.toString(16).padStart(2, '0'))
            .join('');

    // -----------------------------
    // STORE EVERYTHING
    // -----------------------------

    sessionStorage.setItem(
        'helixVaultData',
        JSON.stringify({

            name: f.name,

            size: f.size,

            type: f.type || 'Unknown',

            binary: binary,

            dna: dna,

            dnaLength: dna.length,

            gcContent: gcContent,

            longestHomopolymer:
                longestHomopolymer,

            sha256: sha256

        })
    );

    status.textContent =
        `✓ ${f.name} analyzed successfully`;

    setTimeout(() => {
        location.href = 'storage.html';
    }, 500);

});