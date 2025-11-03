module.exports = {
    content: [
        './templates/**/*.html',
    ],
    daisyui: {
        styled: true,
        themes: [
            {
                light: {
                    ...require('daisyui/src/theming/themes')['light'],
                    '--rounded-box': '0.35rem',
                    '--rounded-btn': '0.35rem',
                    '--rounded-badge': '1.9rem',
                    '--animation-btn': '0.25s',
                    '--animation-input': '0.2s',
                    '--btn-focus-scale': '0.95',
                    '--border-btn': '1px',
                    '--tab-border': '1px',
                    '--tab-radius': '0.5rem',
                    '--pc': '100% 0.038956 4.763163;'
                }
            }
        ]
    },
    plugins: [
        require('daisyui'),
    ],
}

