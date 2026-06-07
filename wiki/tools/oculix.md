---
title: OculiX
type: technology
created: 2026-06-05
last_updated: 2026-06-07
domain: tools
related: ["agent-aget", "Antfarm", "Mermaid", "MCPorter", "OpenScreen"]
sources: ["github-oculix-org-oculix-2026-06-05"]
tags: ["tools", "automation", "workflow", "computer-vision", "ocr"]
---

# OculiX

`OculiX` — open-source visual automation IDE и runtime для автоматизации графических интерфейсов по тому, как они выглядят на экране. Вместо DOM selectors, accessibility hooks или XPath он работает с pixels, screenshots, template matching и OCR.

Практически это инструмент для случаев, где selector-based automation ломается или невозможна: native desktop apps, Citrix/RDP/VNC, Canvas/WebGL UI, multi-application workflows, Android через ADB и любые окружения, где пользователь видит итоговый экран, но структура интерфейса недоступна или нестабильна.

## Что делает

OculiX продолжает lineage Sikuli / SikuliX и даёт пользователю visual scripting слой:

- искать элементы по картинкам и screenshots;
- кликать, ждать, вводить текст и управлять GUI;
- использовать OCR для текстового распознавания;
- автоматизировать локальные и удалённые экраны;
- запускать скрипты на Windows, macOS и Linux;
- работать через IDE или JVM scripting environment.

Первый скрипт выглядит как визуальный сценарий: `click("file_menu.png")`, `wait("save_dialog.png")`, `type("filename_field.png", "report_today.csv")`. Это снижает порог входа: если пользователь может сделать screenshot элемента, он может собрать базовую автоматизацию.

## Visual automation model

Главная идея OculiX — автоматизация не по внутренней структуре приложения, а по видимому результату. OpenCV-based matching ищет шаблоны на экране, учитывая DPI, similarity tuning и несколько стратегий matching перед ошибкой `FindFailed`.

Такой подход особенно полезен для legacy и enterprise-сценариев, где приложение может быть старым, закрытым, виртуализированным или canvas-rendered. Там, где Playwright/Selenium/Appium требуют DOM, accessibility tree или стабильные selectors, OculiX может работать по картинке.

С [agent-aget]({{ '/wiki/tools/agent-aget' | relative_url }}) связь концептуальная: agent-aget даёт LLM-агенту CLI-доступ к браузерному workflow, а OculiX решает более широкий visual automation слой — не только web page, но и desktop/remote/mobile GUI.

## OCR и remote execution

В README выделены два OCR-направления:

- Tesseract embedded через Legerix без ручной установки;
- PaddleOCR как opt-in HTTP server для multilingual и CJK workloads.

Для удалённых окружений есть full VNC stack: `VNCScreen`, `VNCRobot`, X keysym mapping и thread-safe parallel sessions. Также есть native SSH tunneling через `SSHTunnel` на JSch, чтобы открывать tunnels из Java без внешних shell wrappers.

## Runtime и языки

OculiX требует Java 11+ и распространяется как Maven dependency `io.github.oculix-org:oculixapi`. Основной scripting слой — Jython с Python 2.7 syntax и JVM interop. README также указывает поддержку JRuby, Robot Framework и PowerShell runners.

Это делает OculiX ближе к полноценному automation platform, чем к одному CLI helper: пользователь может писать быстрые visual scripts, а разработчик — использовать JVM ecosystem и интегрировать automation в более крупный процесс.

## Где уместен

OculiX подходит для:

- desktop GUI automation;
- RPA-подобных процессов без коммерческой платформы;
- тестирования и автоматизации приложений без стабильных selectors;
- remote desktop automation через VNC/RDP/Citrix;
- Android automation через ADB без Appium/XPath/accessibility API;
- визуального контроля интерфейсов, где важен именно экранный результат.

В долгих процессах OculiX может быть executor step внутри [Antfarm]({{ '/wiki/tools/antfarm' | relative_url }}) или похожего workflow engine: OculiX управляет видимым UI, а orchestration layer хранит состояние процесса, расписание и следующий шаг.

## Сравнение с RPA и browser automation

По README, OculiX позиционируется рядом с RPA и visual automation tools вроде UiPath и Eggplant, но отличается MIT-лицензией, local/self-hosted model и cross-platform запуском. В отличие от UiPath, он не опирается прежде всего на UI selectors; в отличие от обычного browser automation, он работает с любым экраном, включая native apps и виртуальные рабочие столы.

С [Mermaid]({{ '/wiki/tools/mermaid' | relative_url }}) связь прикладная: visual automation workflows часто полезно документировать как sequence/flow diagrams, особенно когда один сценарий управляет несколькими приложениями, удалёнными экранами и условиями ожидания. [OpenScreen]({{ '/wiki/tools/openscreen' | relative_url }}) дополняет этот слой как recorder/editor: OculiX может исполнять GUI-сценарий, а OpenScreen — сохранить результат как демо или evidence video.

## Ограничения и осторожность

Visual automation менее привязана к DOM/selectors, но имеет свои риски:

- screenshots могут ломаться из-за темы, DPI, языка интерфейса или layout changes;
- OCR зависит от качества изображения и языка;
- Jython Python 2.7 syntax может быть непривычен современным Python-разработчикам;
- remote desktop automation требует аккуратной работы с latency, focus и session state;
- автоматизация GUI должна учитывать права пользователя и правила эксплуатации целевой системы.

Также важно различать visual automation и semantic understanding: OculiX надёжно действует по видимым patterns, но бизнес-логика сценария всё равно должна быть явно описана и проверена.

## Практический вывод

`OculiX` полезен там, где нужно автоматизировать то, что видно на экране, а не то, что доступно через API или selectors. Его сильная сторона — универсальность visual model: desktop, remote, browser-like canvas UI и mobile scenarios можно описывать одним подходом через screenshots, OCR и GUI actions.

## Источники

- https://github.com/oculix-org/Oculix
- https://oculix.org
