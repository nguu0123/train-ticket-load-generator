#!/bin/bash
docker buildx build --platform=linux/arm64,linux/amd64 -t rdsea/train_ticket_loadgen:latest ..
