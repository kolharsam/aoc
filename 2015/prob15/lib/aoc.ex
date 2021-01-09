# NOTE: I should be writing better TypeSpecs for the methods in here

defmodule AOC do
  @spec parse_ingredients(binary) :: nil | map
  def parse_ingredients(line) do
    pattern =
      ~r/(?<item>\w+): capacity (?<capacity>-?\d+), durability (?<durability>-?\d+), flavor (?<flavor>-?\d+), texture (?<texture>-?\d+), calories (?<calories>-?\d+)/

    Regex.named_captures(pattern, line)
  end

  @spec read_file :: [binary]
  def read_file do
    file_lines = File.read!("lib/15.in")
    String.split(file_lines, "\n")
  end

  @spec get_combos :: [any]
  # there should be a better way to do this than this list comprehension
  # although there are recursive techniques we can use to generate all the
  # possible combinations, but I feel that this approach works well if we
  # know the number of numbers involved
  def get_combos() do
    for x <- 1..100, y <- 1..100, z <- 1..100, w <- 1..100, x + y + z + w == 100, do: {x, y, z, w}
  end

  @spec calc_sum(any) :: any
  def calc_sum(zl) do
    zl
    |> Enum.reduce(0, fn x, acc ->
      acc + elem(x, 0) * elem(x, 1)
    end)
  end

  @spec get_prop_list(any, any) :: [any]
  def get_prop_list(li, prop) do
    for ing <- li, do: elem(Integer.parse(ing[prop]), 0)
  end

  # includes the code for part 2 too
  @spec calc_score(any, any, any, any, any) :: {number, [any]}
  def calc_score(ing_list, x, y, z, w) do
    vals = [x, y, z, w]

    caps = get_prop_list(ing_list, "capacity")
    durs = get_prop_list(ing_list, "durability")
    flas = get_prop_list(ing_list, "flavor")
    texs = get_prop_list(ing_list, "texture")
    # for part 2
    cals = get_prop_list(ing_list, "calories")

    s_caps = calc_sum(Enum.zip(vals, caps))
    s_durs = calc_sum(Enum.zip(vals, durs))
    s_flas = calc_sum(Enum.zip(vals, flas))
    s_texs = calc_sum(Enum.zip(vals, texs))
    # for part 2
    s_cals = calc_sum(Enum.zip(vals, cals))

    if s_caps < 0 or s_durs < 0 or s_flas < 0 or s_texs < 0 do
      {0, s_cals}
    else
      {s_caps * s_durs * s_flas * s_texs, s_cals}
    end
  end

  @spec find_best_combo(any, any) :: {number, number}
  def find_best_combo(list, combos) do
    filtered_list =
      combos
      |> Enum.map(fn {x, y, z, w} ->
        score = calc_score(list, x, y, z, w)
        {x, y, z, w, elem(score, 0), elem(score, 1)}
      end)
      |> Enum.filter(fn sc -> elem(sc, 4) != 0 end)

    p1 =
      filtered_list
      |> Enum.map(fn x -> elem(x, 4) end)
      |> Enum.max()

    p2 =
      filtered_list
      |> Enum.map(fn x -> {elem(x, 4), elem(x, 5)} end)
      |> Enum.filter(fn x -> elem(x, 1) == 500 end)
      |> Enum.map(fn x -> elem(x, 0) end)
      |> Enum.max()

    {p1, p2}
  end

  @spec find_best_mix(any) :: any
  def find_best_mix(parsed_list) do
    combos = get_combos()
    find_best_combo(parsed_list, combos)
  end

  @spec run :: any
  def run do
    lines = read_file()
    parsed_lines = Enum.map(lines, fn x -> parse_ingredients(x) end)
    find_best_mix(parsed_lines)
  end
end
