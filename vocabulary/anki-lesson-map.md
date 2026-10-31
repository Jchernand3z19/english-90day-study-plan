# Anki-to-lesson thematic map

**Source:** `guia_orden_anki_90_dias.csv` (1,000 ordered records).  
**Last reviewed:** 2026-10-31.  
**Status:** thematic alignment map; exact card-by-card daily assignment and audio quality review remain pending.

## Data integrity check

The available CSV contains 1,000 rows and eight populated columns: order, phase, phase tag, category, English phrase, Spanish translation, audio reference, and Anki note ID.

| Check | Result |
|---|---:|
| Total records | 1,000 |
| Phase 1 | 340 |
| Phase 2 | 355 |
| Phase 3 | 305 |
| Categories | 41 |
| Missing values in the eight fields | 0 |
| Duplicate note IDs | 0 |
| Audio references listed | 1,000 |
| Repeated English wording | 10 repeated English-phrase pairs (20 rows) retained |

The 10 repeated English wordings occur in different categories/phases. They were not removed automatically because context, translation, or intended use may differ. They should be reviewed before any future deduplication.

**Important boundary:** the CSV confirms that 1,000 audio filenames are referenced. It does not prove that the corresponding media files were listened to, that each recording is clear/natural, or that accent and pronunciation are consistent. The previous package inspection found all referenced media filenames in the APKG media map; audio quality remains unverified.

## How to use this map

- The phase and category identify the broad learning area; they do **not** assign every card to one exact day.
- Each lesson should retrieve only a small, relevant selection, normally one to three familiar phrases at the start, with more only when workload and recall justify it.
- Do not force unrelated phrases into a conversation. The tutor may introduce natural supporting language that is not in Anki.
- A phrase can be reused across multiple lessons when the communicative purpose changes.
- A correct Anki response is retrieval evidence, not proof of listening or spoken mastery.
- Use the original card spelling. Keep pronunciation notes in lesson guidance, not respelled card text.

## Category-to-lesson thematic alignment

The day ranges below identify the most relevant lesson topics, not a strict daily quota or an exact card schedule.

### Phase 1 — Foundations and daily life (340 phrases)

| Anki category | Cards | Order range | Relevant lesson topics |
|---|---:|---:|---|
| Saludos y Despedidas | 15 | 1–15 | Days 1–7: greetings, names, introductions, closing |
| Cortesía y Social | 20 | 16–35 | Days 2–4, 8–13: polite responses, requests, everyday service exchanges |
| Para cuando no entiendes | 15 | 36–50 | Days 4, 12, 17–20: repetition, clarification, asking for help |
| Información Personal | 20 | 51–70 | Days 1, 3, 6: name, origin, city, short introduction |
| El Tiempo y la Hora | 15 | 71–85 | Days 22–23, 31–36: times, schedules, simple confirmations |
| Situaciones Diarias | 30 | 86–115 | Days 22–30: routines, daily actions, short descriptions |
| De Compras | 25 | 116–140 | Days 8–9, 13: prices, sizes, preferences, payment |
| En el Restaurante | 30 | 141–170 | Days 10–11: ordering, polite requests, simple restaurant exchanges |
| En la Cocina y Comida | 30 | 171–200 | Days 10–11, 24, 54: food, meals, preferences, interests |
| Direcciones | 20 | 201–220 | Days 15–20, 35: locations, directions, distance |
| Frases para la Calle y el Entorno | 25 | 221–245 | Days 15–20, 31–37: public places, transport, getting around |
| En Casa | 25 | 246–270 | Days 22, 26–27: home and daily routines |
| Hobbies y Tiempo Libre | 25 | 271–295 | Days 5, 24, 52–58: preferences, free time, social conversation |
| Relaciones y Vida Social | 25 | 296–320 | Days 6, 24, 52–58: introductions, interests, social exchanges |
| Describiendo Personas | 20 | 321–340 | Days 24–27, 52–58: people, preferences, everyday descriptions |

### Phase 2 — Practical communication (355 phrases)

| Anki category | Cards | Order range | Relevant lesson topics |
|---|---:|---:|---|
| Viajes y Transporte | 25 | 341–365 | Days 31–37, 49–50: travel, transport, bookings, unexpected changes |
| En el Trabajo | 30 | 366–395 | Days 25, 75–81: work tasks, professional introductions, meetings |
| Teléfono y Tecnología | 25 | 396–420 | Days 45–50, 78: communication, devices, practical problems |
| Salud y Emergencias | 30 | 421–450 | Days 45–50: needs, problems, asking for help |
| Sentimientos y Estados de Ánimo | 25 | 451–475 | Days 41–44, 52–58: reactions, experiences, social conversation |
| Educación y Aprendizaje | 25 | 476–500 | Days 61–67, 82: learning, opinions, explaining processes |
| Dinero y Finanzas | 25 | 501–525 | Days 8, 31–36, 45–50: prices, costs, payments, practical issues |
| Trámites y Documentos | 25 | 526–550 | Days 12, 32–36, 78: forms, reservations, confirmation, documents |
| Hablando del Pasado | 25 | 551–575 | Days 38–44, 59: past actions and experiences |
| Planes y Futuro | 25 | 576–600 | Days 31–36, 53–56: plans, arrangements, invitations |
| Eventos y Celebraciones | 25 | 601–625 | Days 43–44, 53–58: events, invitations, social plans |
| Describiendo Experiencias | 25 | 626–650 | Days 38–44, 61–65: stories, experiences, reactions |
| Deseos y Necesidades | 25 | 651–675 | Days 45–50, 52–58: requests, preferences, needs |
| Preguntas Frecuentes y Misceláneas | 20 | 676–695 | Use selectively wherever the communicative context fits; no forced day assignment |

### Phase 3 — Opinions and nuance (305 phrases)

| Anki category | Cards | Order range | Relevant lesson topics |
|---|---:|---:|---|
| Expresando Opiniones y Gustos | 30 | 696–725 | Days 24, 54, 61–67: preferences, opinions, reasons |
| Comparaciones y Cantidades | 25 | 726–750 | Days 64, 82–84: comparisons, advantages, quantities |
| Discusiones y Malentendidos | 25 | 751–775 | Days 48, 63, 70–73, 86: disagreement, clarification, repair |
| Expresando Certeza y Duda | 25 | 776–800 | Days 61–74, 85–87: confidence, uncertainty, responses |
| Phrasal Verbs y Expresiones Comunes | 25 | 801–825 | Days 69, 73–74, 82, 86–87: common phrasal verbs in context |
| Modismos y Expresiones Idiomáticas | 30 | 826–855 | Days 68, 73–74, 87: idioms in natural conversation |
| Expresiones para Situaciones Específicas | 25 | 856–880 | Days 61–87: context-specific interaction |
| Frases Avanzadas para Debatir | 25 | 881–905 | Days 62–67, 82–84: discussion, reasons, balanced views |
| Proverbios y Sabiduría Popular | 25 | 906–930 | Days 68–74, 87: figurative meaning and context |
| Preguntas para Profundizar | 20 | 931–950 | Days 42, 52–57, 65, 87: follow-up and deeper questions |
| Motivación y Ánimo | 25 | 951–975 | Days 51, 58, 90: encouragement and reflection |
| Despedidas y Cierre Final | 25 | 976–1000 | Days 2, 6, 52–58, 80, 87, 90: natural conversation closings |

## Next steps for exact mapping and audio quality

1. Use the APKG and manifest together to verify that each note ID, phrase, and audio file matches; the CSV alone cannot prove the media payload is correct.
2. Create an exact lesson-to-card selection only after reviewing each lesson's taught language and objective. Avoid a mechanical 13-card/day mapping.
3. Sample audio across all three phases and categories, then expand the review where pronunciation, clarity, accent, or text/audio mismatch is found.
4. During the learner pilot, record separately whether a phrase was recalled, understood in audio, and used in a natural response.
