-- Script to list records with score >= 10 from second_table sorted by score
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
