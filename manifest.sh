docker manifest create --amend ctrlaltdev/impulse:latest ctrlaltdev/impulse:amd64-latest ctrlaltdev/impulse:arm32v6-latest ctrlaltdev/impulse:arm64v8-latest
docker manifest annotate ctrlaltdev/impulse:latest ctrlaltdev/impulse:arm32v6-latest --os linux --arch arm
docker manifest annotate ctrlaltdev/impulse:latest ctrlaltdev/impulse:arm64v8-latest --os linux --arch arm64 --variant armv8
docker manifest push --purge ctrlaltdev/impulse:latest