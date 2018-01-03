from runner.processors import DockerProcessor


def test_connect_to_docker_client():
    docker_processor = DockerProcessor()
    assert docker_processor.client is not None


def test_execute_container():
    docker_processor = DockerProcessor()
    client = docker_processor.client
    container = client.containers.run(
        "localhost:5000/dummy_process", stdout=True, remove=True, detach=True)

    assert b'hello' in container.logs()

