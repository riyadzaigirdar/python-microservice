## GET inside docker contaner and migrate

    $: docker-compose exec app sh

    $: python manager.py db init

    $: python manager.py db migrate

    $: python manager.py db upgrade