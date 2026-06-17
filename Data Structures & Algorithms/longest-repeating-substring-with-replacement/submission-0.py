class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        max_count = 0  # maior frequência dentro da janela
        result = 0

        for right in range(len(s)):
            # 1. Expande a janela: adiciona s[right]
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # 2. Janela inválida? (precisaria de mais de k substituições)
            window_size = right - left + 1
            if window_size - max_count > k:
                # Remove s[left] da contagem e contrai
                count[s[left]] -= 1
                left += 1

            # 3. Atualiza resultado
            result = max(result, right - left + 1)

        return result