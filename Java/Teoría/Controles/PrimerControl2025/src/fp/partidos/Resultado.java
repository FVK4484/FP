package fp.partidos;

public record Resultado(Integer minuto, Integer golesLocal, Integer golesVisitante) implements Comparable<Resultado>{
	
	public Resultado {
		checkMinuto(minuto);
		checkGolesLocal(golesLocal);
		checkGolesVisitante(golesVisitante);
	}
	
	private void checkMinuto(Integer minuto) {
		if (minuto < 0) {
			throw new IllegalArgumentException("El minuto debe ser mayor o igual a 0.");
		}
	}
	
	private void checkGolesLocal(Integer golesLocal) {
		if (golesLocal < 0) {
			throw new IllegalArgumentException("Los goles del equipo local deben ser mayores o iguales a 0.");
		}
	}

	private void checkGolesVisitante(Integer golesVisitante) {
		if (golesVisitante < 0) {
			throw new IllegalArgumentException("Los goles del equipo visitante deben ser mayores o iguales a 0.");
		}
	}
	
	public Integer getDiferenciaGoles() {
		return golesLocal - golesVisitante;
	}
	
	public static Resultado parse(String formato) {
		
		String [] trozos = formato.split("-");
		Integer minuto = Integer.valueOf(trozos[0].trim());
		Integer golesLocal = Integer.valueOf(trozos[1].trim());
		Integer golesVisitante = Integer.valueOf(trozos[2].trim());
		return new Resultado(minuto, golesLocal, golesVisitante);
		
	}

	public int compareTo(Resultado r) {
		Integer res = minuto.compareTo(r.minuto);
		if (res == 0) {
			res = getDiferenciaGoles().compareTo(r.getDiferenciaGoles());
			if (res == 0) {
				res = golesLocal.compareTo(r.golesLocal());
				if (res == 0) {
					res = golesVisitante.compareTo(r.golesVisitante);
				}
			}
		}
		return res;
	}
	
}
