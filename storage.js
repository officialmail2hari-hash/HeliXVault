const raw = sessionStorage.getItem('helixVaultData');

if (!raw) {
    location.href = 'index.html';
}

else {

    const d = JSON.parse(raw);

    // -----------------------------
    // DIGITAL DATA
    // -----------------------------

    document.getElementById('name')
        .textContent = d.name;

    document.getElementById('size')
        .textContent = formatSize(d.size);

    document.getElementById('type')
        .textContent = d.type;

    // -----------------------------
    // SHA-256
    // -----------------------------

    document.getElementById('hash')
        .textContent = d.sha256;

    // -----------------------------
    // BINARY
    // -----------------------------

    const binaryChunks =
        d.binary.match(/.{1,32}/g) || [];

    document.getElementById('binary')
        .textContent =
            binaryChunks
                .slice(0, 5)
                .join('\n');

    // -----------------------------
    // DNA
    // -----------------------------

    const dnaChunks =
        d.dna.match(/.{1,20}/g) || [];

    document.getElementById('dna')
        .textContent =
            dnaChunks
                .slice(0, 6)
                .join(' ');

    // -----------------------------
    // DNA ANALYSIS
    // -----------------------------

    document.getElementById('dnaLength')
        .textContent =
            `${d.dnaLength} bases`;

    document.getElementById('gcContent')
        .textContent =
            `${d.gcContent.toFixed(2)}%`;

    document.getElementById('homopolymer')
        .textContent =
            d.longestHomopolymer;

    // -----------------------------
    // PROGRESS
    // -----------------------------

    let p = 0;

    const fill =
        document.getElementById('fill');

    const percent =
        document.getElementById('percent');

    const status =
        document.getElementById('statusText');

    const stages = [
        'READING DIGITAL DATA',
        'CONVERTING TO BINARY',
        'MAPPING BITS → A C G T',
        'ANALYZING DNA SEQUENCE',
        'DNA STORAGE COMPLETE'
    ];

    const timer = setInterval(() => {

        p = Math.min(
            100,
            p + 2 + Math.floor(Math.random() * 5)
        );

        fill.style.width = p + '%';

        percent.textContent =
            p + '%';

        status.textContent =
            stages[
                Math.min(
                    stages.length - 1,
                    Math.floor(p / 25)
                )
            ];

        if (p >= 100) {
            clearInterval(timer);
        }

    }, 140);

    // -----------------------------
    // FLOATING BINARY
    // -----------------------------

    const holder =
        document.getElementById(
            'floatingBinary'
        );

    function addBit() {

        const e =
            document.createElement('span');

        e.className =
            'bit' +
            (Math.random() > .5
                ? ' pink'
                : '');

        e.textContent =
            Math.random() > .5
                ? '10100110'
                : '01011001';

        e.style.left =
            (Math.random() * 100) + '%';

        e.style.top =
            (15 + Math.random() * 70) + '%';

        e.style.setProperty(
            '--x',
            ((Math.random() > .5 ? 1 : -1) *
            (180 + Math.random() * 380)) + 'px'
        );

        e.style.setProperty(
            '--y',
            (-120 + Math.random() * 240) + 'px'
        );

        holder.appendChild(e);

        setTimeout(
            () => e.remove(),
            5000
        );
    }

    for (let i = 0; i < 32; i++) {
        setTimeout(addBit, i * 100);
    }

    setInterval(addBit, 260);
}


function formatSize(n) {

    const u =
        ['B', 'KB', 'MB', 'GB'];

    let i =
        Math.floor(
            Math.log(n || 1) /
            Math.log(1024)
        );

    i = Math.min(i, u.length - 1);

    return `${(n / 1024 ** i)
        .toFixed(i ? 2 : 0)} ${u[i]}`;
}