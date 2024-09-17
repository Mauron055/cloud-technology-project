Ссылки на реджистри и работа с репозиторием:

- cd C:\Users\User\de-project-sprint-9\solution
- docker compose up -d --build
- cd C:\Users\User\de-project-sprint-9\solution\service_dds
- docker build . -t cr.yandex/crp9ma5c91topbr50lv9/dds_service:v2024-03-09-r1
- docker push cr.yandex/crp9ma5c91topbr50lv9/dds_service:v2024-03-09-r1
- helm upgrade --install --atomic dds-service app -n c24-tarasov-danila
- cd C:\Users\User\de-project-sprint-9\solution\service_cdm
- docker build . -t cr.yandex/crp9ma5c91topbr50lv9/cdm_service:v2024-03-09-r1
- docker push cr.yandex/crp9ma5c91topbr50lv9/cdm_service:v2024-03-09-r1
- helm upgrade --install --atomic cdm-service app -n c24-tarasov-danila
