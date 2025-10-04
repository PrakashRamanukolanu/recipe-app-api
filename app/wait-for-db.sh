#!/bin/sh

set -e

cmd="$@"

until pg_isready -h "$DB_HOST" -U "$DB_USER" >/dev/null 2>&1; do
    echo "Database Unavailable - trying again"
    sleep 2
done

echo "Database is running....continuing operations"
exec $cmd

