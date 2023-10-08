class Solution:
    def validIPAddress(self, queryIP: str) -> str:

        if len(queryIP) > 39:
            return "Neither"
        
        if "." in queryIP:
            parts = queryIP.split('.')
            if len(parts) != 4:
                return "Neither"
            for part in parts:
                if not part.isdigit():
                    return "Neither"
                if not 0 <= int(part) < 256:
                    return "Neither"
                if str(int(part)) != part:
                    return "Neither"
            return "IPv4"
        if ":" in queryIP:
            parts = queryIP.split(":")
            if len(parts) != 8:
                return "Neither"
            for part in parts:
                if not 0 < len(part) < 5:
                    return "Neither"
                for c in part:
                    if c not in "ABCDEFabcdef0123456789":
                        return "Neither"
            return "IPv6"
        return "Neither"